resource "aws_lambda_permission" "allow_api_gateway_to_invoke_lambdas" {
  for_each      = var.lambdas
  statement_id  = "AllowExecutionFromApiGateway"
  action        = "lambda:InvokeFunction"
  function_name = each.value["name"]
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api.execution_arn}/*/*/*"
}