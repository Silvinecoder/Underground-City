resource "aws_lambda_function" "flask_lambda" {
  function_name    = "${var.project_name}-backend"
  role             = aws_iam_role.lambda_exec_role.arn
  handler          = var.lambda_handler
  runtime          = var.runtime
  timeout          = 30
  memory_size      = 256
  source_code_hash = filebase64sha256(var.lambda_zip)
  filename         = var.lambda_zip

  environment {
  variables = {
    DB_NAME       = var.db_name
    DB_USERNAME   = var.db_username
    DB_PASSWORD   = var.db_password
  }
}

  vpc_config {
    subnet_ids         = var.subnet_ids
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
}