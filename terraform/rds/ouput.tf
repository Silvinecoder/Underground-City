output "db_endpoint" {
  value = aws_db_instance.underground_db.endpoint
}

output "rds_arn" {
  value = aws_db_instance.underground_db.arn
}

output "db_password" {
  value     = random_password.db_password.result
  sensitive = true
}