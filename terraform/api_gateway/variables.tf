variable "project_name" {}
variable "region" {}
variable "top_domain" {}
variable "subdomain" {}
variable "cert_arn" {}
variable "name" {}
variable "lambdas" {
  type = map(object({
    arn  = string
    name = string
  }))
}
