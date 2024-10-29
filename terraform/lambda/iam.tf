resource "aws_iam_role_policy" "lambda_policy" {
  name   = "${var.project_name}_lambda_read_only_policy"
  role   = aws_iam_role.lambda_exec_role.id

  policy = jsonencode({
  Version = "2012-10-17",
  Statement = [
    {
      Action   = [
        "rds:DescribeDBInstances",
        "rds:Connect"
      ],
      Effect   = "Allow",
      Resource = var.rds_arn
    },
    {
      Action   = [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      Effect   = "Allow",
      Resource = "arn:aws:logs:*:*:*"
    }
  ]
})
}
