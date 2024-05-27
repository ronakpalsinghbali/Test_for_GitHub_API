provider "aws" {
  region = var.region
}


resource "aws_instance" "example_server" {
  ami           = "ami-04e91463"
  instance_type = "t2.micr"

  tags = {
    Name = "JacksBlogExample"
  }
}