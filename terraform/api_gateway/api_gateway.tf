resource "aws_api_gateway_rest_api" "api" {
  name = "${var.name}-${var.env}"
  body = templatefile(var.open_api_spec_file, merge({
    region = var.region

    server_environment = var.env
    server_url         = "https://${var.subdomain}${var.subdomain_suffix}.${var.top_domain}"
  }, zipmap([for k, v in var.lambdas : "${k}_lambda_arn"], [for k, v in var.lambdas : v["arn"]])))

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id       = aws_api_gateway_rest_api.api.id
  stage_name        = var.env
  description       = "Deployed at ${timestamp()}"
  stage_description = "${var.env}: Deployed at ${timestamp()}"
}

resource "aws_api_gateway_gateway_response" "cors4xx" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  response_type = "DEFAULT_4XX"

  response_parameters = {
    "gatewayresponse.header.Access-Control-Allow-Origin"  = "'*'"
    "gatewayresponse.header.Access-Control-Allow-Methods" = "'GET, POST, PUT, DELETE, OPTIONS'"
    "gatewayresponse.header.Access-Control-Allow-Headers" = "'*'"
  }
}

resource "aws_api_gateway_gateway_response" "cors5xx" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  response_type = "DEFAULT_5XX"

  response_parameters = {
    "gatewayresponse.header.Access-Control-Allow-Origin"  = "'*'"
    "gatewayresponse.header.Access-Control-Allow-Methods" = "'GET, POST, PUT, DELETE, OPTIONS'"
    "gatewayresponse.header.Access-Control-Allow-Headers" = "'*'"
  }
}