resource "aws_api_gateway_domain_name" "domain" {
  domain_name              = "${var.subdomain}.${var.top_domain}"
  regional_certificate_arn = var.cert_arn

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_base_path_mapping" "domain_mapping" {
  api_id      = aws_api_gateway_rest_api.api.id
  domain_name = aws_api_gateway_domain_name.domain.domain_name
}