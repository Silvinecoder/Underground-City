output "lambda_arn" {
  value = aws_lambda_function.flask_lambda.arn
}

output "lambda_sg_id" {
  value = aws_security_group.lambda_sg.id
}
