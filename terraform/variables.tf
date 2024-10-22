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

variable "db_password" {
  description = "Database password for RDS"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "Database name for RDS"
  type        = string
}

variable "custom_domain" {
  description = "Custom domain name for the API Gateway"
  type        = string
}

variable "certificate_arn" {
  description = "ARN of the SSL certificate for the custom domain"
  type        = string
}

variable "vpc_id" {
  description = "ID of the VPC to deploy RDS in"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for RDS deployment"
  type        = list(string)
}
