provider "aws" {
  region = var.region
}

module "lambda" {
  source        = "./lambda"
  project_name  = var.project_name
  lambda_zip    = var.lambda_zip
  lambda_handler = var.lambda_handler
  runtime       = var.runtime
  db_username   = var.db_username
  db_password   = var.db_password
  db_name       = var.db_name
  rds_arn       = module.rds.rds_arn
}

module "api_gateway" {
  source       = "./api_gateway"
  project_name = var.project_name
  lambda_arn   = module.lambda.lambda_arn
  region       = var.region
  custom_domain = var.custom_domain
  certificate_arn = var.certificate_arn
}

module "rds" {
  source       = "./rds"
  project_name = var.project_name
  db_username  = var.db_username
  db_password  = var.db_password
  db_name      = var.db_name
  vpc_id       = var.vpc_id
  subnet_ids   = var.subnet_ids
}