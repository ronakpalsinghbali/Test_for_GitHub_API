provider "aws" {
  region = "ap-south-1"
}

resource "aws_db_subnet_group" "this" {
  name       = "test"
  subnet_ids = ["subnet-07d0a19dba27e6703", "subnet-001e69de25e3fd631"]
}

# variable "subnet_ids" {
#   type    = list(string)
# }

