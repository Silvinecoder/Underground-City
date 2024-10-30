variable "project_name" {}
variable "region" {}
variable "top_domain" {
  description = "The main domain for the API"
  type        = string
}

variable "subdomain" {
  description = "The subdomain for the API"
  type        = string
}

variable "cert_arn" {}
variable "name" {}
variable "lambdas" {
  type = map(object({
    arn  = string
    name = string
  }))
}
