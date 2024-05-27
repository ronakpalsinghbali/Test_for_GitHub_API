provider "aws" {
  region = var.region
}


resource "aws_vpc" "my_vpc" {
  cidr_block = "172.16.0.0/"

  tags = {
    Name = "tf-example"
  }
}