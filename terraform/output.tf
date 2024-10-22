output "db_endpoint" {
  value = module.rds.db_endpoint
}

output "lambda_function_arn" {
  value = module.lambda.lambda_arn
}

output "api_gateway_url" {
  value = module.api_gateway.api_gateway_url
}