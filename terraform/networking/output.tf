output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_ids" {
  value = [
    aws_subnet.subnet_1.id,
    aws_subnet.subnet_2.id,
  ]
}
