variable "lambda_subnet_ids" {
  type = list(string)
  default = [ "" ]
}

variable "rds_subnet_ids" {
  type = list(string)
  default = [ "" ]
}