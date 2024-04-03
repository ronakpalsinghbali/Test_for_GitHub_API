provider "aws" {
  region = "ap-south-1"
}

resource "aws_db_subnet_group" "this" {
  name       = "test"
  subnet_ids = var.subnet_ids
}

variable "subnet_ids" {
  type    = list(string)
  default = []
}

output "db_subnet_group" {
  value = aws_db_subnet_group.this.id
}
