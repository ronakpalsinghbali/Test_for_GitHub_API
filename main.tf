provider "aws" {
  region = var.region
}

resource "aws_db_subnet_group" "lambda" {
  name       = "test"
  subnet_ids = var.lambda_subnet_ids
}

resource "aws_db_subnet_group" "rds" {
  name       = "test2"
  subnet_ids = var.rds_subnet_ids
}
