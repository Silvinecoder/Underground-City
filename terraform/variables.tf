variable "region" {
  description = "The AWS region to deploy resources in"
  type        = string
}

variable "project_name" {
  description = "The name of the project"
  type        = string
}

variable "lambda_zip" {
  description = "Path to the Lambda deployment package"
  type        = string
}

variable "lambda_handler" {
  description = "Lambda handler (e.g. app.lambda_handler)"
  type        = string
}

variable "runtime" {
  description = "Runtime for Lambda"
  type        = string
  default     = "python3.9"
}

variable "db_username" {
  description = "Database username for RDS"
  type        = string
}
variable "db_name" {
  description = "Database name for RDS"
  type        = string
}

variable "cert_arn" {
  description = "ARN of the SSL certificate for the custom domain"
  type        = string
}

variable "top_domain" {
  description = "The top-level domain name (e.g., example.com)"
  type        = string
}

variable "subdomain" {
  description = "The subdomain for the API Gateway (e.g., api)"
  type        = string
}
