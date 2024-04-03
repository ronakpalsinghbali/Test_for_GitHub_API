provider "aws" {
  region = "ap-south-1"
}

resource "aws_db_subnet_group" "this" {
  name       = "test"
  subnet_ids = var.dp_subnet_ids
}


