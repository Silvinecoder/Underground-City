output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_ids" {
  value = [
    aws_subnet.subnet_1.id,
    aws_subnet.subnet_2.id,
  ]
}

output "lambda_sg" {
  description = "The security group ID for the Lambda function"
  value       = aws_security_group.lambda_sg.id
}

output "rds_sg" {
  description = "The security group ID for the RDS instance"
  value       = aws_security_group.rds_sg.id
}