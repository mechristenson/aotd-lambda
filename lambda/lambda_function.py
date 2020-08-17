import os
import sys
import uuid
from urllib.parse import unquote_plus

import boto3

from spotify_client import *

s3_client = boto3.client('s3')

def lambda_handler(event, context):
  for record in event['Records']:
    print(record)
    bucket = record['bucket']
    key = unquote_plus(record['key'])
    tmpkey = key.replace('/', '')
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
    s3_client.download_file(bucket, key, download_path)

    client_id, secret = parse_credentials(download_path)
    get_spotify_data(client_id, secret)

def parse_credentials(download_path):
  with open(download_path) as f:
    client_id, secret = [item.split('=')[1].strip() for item in f.readlines()]
  return client_id, secret

def get_spotify_data(client_id, secret):
  spotify = SpotifyAPI(client_id, secret)
  response = spotify.search("AotD 2020", search_type="playlist")
  playlist_id = response['playlists']['items'][0]['id']
  print(playlist_id)
