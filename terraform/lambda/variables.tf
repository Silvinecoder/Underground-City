variable "project_name" {
  description = "Name of the project"
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

variable "rds_arn" {
  description = "The ARN of the RDS instance"
  type        = string
}

variable "db_name" {
  description = "Database name for RDS"
  type        = string
}

variable "db_username" {
  description = "Database username for RDS"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for the Lambda function"
  type        = list(string)
}

variable "db_password" {
  description = "Database password for the Lambda function"
  type        = string
}
