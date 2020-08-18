rm lambda_function_payload.zip
curr=$(pwd)
cd aotd-lambda/lib/python3.8/site-packages/
zip -r9 ${curr}/lambda_function_payload.zip .
cd ${curr}
zip -g lambda_function_payload.zip lambda_function.py
zip -g lambda_function_payload.zip spotify_client.py
zip -g lambda_function_payload.zip album.py