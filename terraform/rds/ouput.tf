output "db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}

output "rds_arn" {
  value = aws_db_instance.postgres.arn
}