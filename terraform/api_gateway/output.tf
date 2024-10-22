output "domain_name" {
    value = aws_api_gateway_domain_name.domain.domain_name
}

output "domain_name_regional" {
    value = aws_api_gateway_domain_name.domain.regional_domain_name
}

output "domain_zone_id" {
    value = aws_api_gateway_domain_name.domain.regional_zone_id
}