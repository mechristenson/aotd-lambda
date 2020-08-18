resource "aws_lambda_function" "aotd_lambda" {
  filename         = "../lambda/lambda_function_payload.zip"
  function_name    = "aotd-lambda"
  role             = aws_iam_role.aotd_lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  memory_size      = 128
  timeout          = 10
  source_code_hash = filebase64sha256("../lambda/lambda_function_payload.zip")
  runtime          = "python3.8"
}
