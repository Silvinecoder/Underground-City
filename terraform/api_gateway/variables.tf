variable "region" {}
variable "env" {}
variable "top_domain" {}
variable "subdomain" {}
variable "subdomain_suffix" {}
variable "cert_arn" {}
variable "name" {}
variable "open_api_spec_file" {}

variable "lambdas" { type = map(object({ arn = string, name = string })) }