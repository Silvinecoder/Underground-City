variable "region" {
  description = "AWS region"
  type        = string
  
}

variable "project_name" {
  description = "Name of the project"
  type        = string
}

variable "vpc_id" {
  description = "The ID of the VPC"
  type        = string
}

variable "db_cidr_block" {
  description = "The CIDR block for the RDS instance or database"
  type        = string
}

variable "lambda_sg_id" {
  description = "Security group ID for the Lambda function"
  type        = string
}