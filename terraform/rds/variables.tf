variable "project_name" {
  description = "Name of the project"
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
  description = "List of subnet IDs for the RDS and Lambda functions"
  type        = list(string)
}

variable "vpc_id" {
  description = "The ID of the VPC where the RDS instance will be created"
  type        = string
}

variable "rds_sg" {
  description = "Security group ID for the RDS instance"
  type        = string
}
