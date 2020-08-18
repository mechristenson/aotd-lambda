rm lambda_function_payload.zip
cd aotd-lambda/lib/python3.8/site-packages/
zip -r9 ~/Developer/personal/aotd-lambda/lambda/lambda_function_payload.zip .
cd ~/Developer/personal/aotd-lambda/lambda/
zip -g lambda_function_payload.zip lambda_function.py
zip -g lambda_function_payload.zip spotify_client.py