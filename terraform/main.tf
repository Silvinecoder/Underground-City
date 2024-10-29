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
  db_password   = module.rds.db_password 
  db_name       = var.db_name
  rds_arn       = module.rds.rds_arn
  subnet_ids    = module.vpc.subnet_ids
}

module "api_gateway" {
  source       = "./api_gateway"
  project_name = var.project_name
  region       = var.region
  name         = var.project_name
  top_domain   = var.top_domain
  subdomain    = var.subdomain
  cert_arn     = var.cert_arn
  lambdas               = {
    "backend_lambda" = {
      arn  = module.lambda.lambda_arn
      name = module.lambda.lambda_name
    }
  }
}

module "rds" {
  source       = "./rds"
  project_name = var.project_name
  db_username  = var.db_username
  db_name      = var.db_name
  vpc_id       = module.vpc.vpc_id
  subnet_ids   = module.vpc.subnet_ids
}