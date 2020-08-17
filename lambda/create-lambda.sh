aws lambda create-function --function-name AotDLambda \
--zip-file fileb://function.zip --handler lambda_function.lambda_handler --runtime python3.8 \
--timeout 30 --memory-size 128 \
--role arn:aws:iam::707455875115:role/lambda-s3-role