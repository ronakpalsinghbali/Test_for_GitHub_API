provider "aws" {
  region = var.region
}


resource "aws_cognito_user_pool" "pool" {
  name = "ronak_USER_pool"
  tags = {
    "Owner"   = "ronak"
    "purpose" = "testing"
  }
}