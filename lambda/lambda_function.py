import json
import os
import sys
import uuid
from urllib.parse import unquote_plus

import boto3

from album import Album
from spotify_client import *

s3_client = boto3.client('s3')

def lambda_handler(event, context):
  for record in event['Records']:
    print(record)
    config_bucket = record['config_bucket']
    key = unquote_plus(record['key'])
    storage_bucket = record['storage_bucket']
    target_file = record['target_file']

    tmpkey = key.replace('/', '')
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
    s3_client.download_file(config_bucket, key, download_path)

    client_id, secret = parse_credentials(download_path)
    album_data = get_spotify_data(client_id, secret)

    upload_path = '/tmp/{}{}'.format(uuid.uuid4(), target_file)

    with open(upload_path, 'w') as outfile:
      json.dump([album.__dict__ for album in album_data], outfile)

    s3_client.upload_file(upload_path, storage_bucket, target_file)

def parse_credentials(download_path):
  with open(download_path) as f:
    client_id, secret = [item.split('=')[1].strip() for item in f.readlines()]
  return client_id, secret

def get_spotify_data(client_id, secret):
  spotify = SpotifyAPI(client_id, secret)

  response = spotify.search("AotD 2020", search_type="playlist")
  playlist_id = response['playlists']['items'][0]['id']
  data = spotify.get_playlist(playlist_id)

  offset, limit = get_offset_params(data)
  data = spotify.get_playlist(playlist_id, component_type="tracks",
                              query_params={"offset": offset, "limit": limit})
  return parse_album_data(data)

def get_offset_params(data):
  total = data['tracks']['total']
  limit = data['tracks']['limit']
  offset = total - limit
  return offset, limit

def parse_album_data(data):
  tracks = data['items']

  albums = []
  for track in tracks:
    album_details = track['track']['album']
    album_name = album_details['name']

    if album_name in [album.name for album in albums]:
      continue
    else:
      name = album_name
      artist = album_details['artists'][0]['name']
      url = album_details['href']
      image = album_details['images'][0]['url']
      release_date = album_details['release_date']
      albums.append(Album(name, artist, url, image, release_date))

  return albums
