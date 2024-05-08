variable "region" {
  type = string
}

#  ------------------VPC----------------
variable "cidr_block" {
  description = "VPC CIDR value"
  type = string
  default = null
}


variable "vpc_tags" {
  description = "Extra Tags to attach"
  type = map(any)
  default = null
}







variable "public_subnet_cidrs" {
  type        = list(string)
  description = "Public Subnet CIDR values"
  default     = null
}

variable "public_subnet_tags" {
  description = "Tags for Public subnets"
  type = map(any)
  default = null
}

variable "public_subnet_name" {
  description = "Name of the Public Subnets"
  type = string
  default = null
}



variable "private_subnet_cidrs" {
  type        = list(string)
  description = "Private Subnet CIDR values"
  default     = null
}

variable "private_subnet_tags" {
  description = "Tags for Private subnets"
  type = map(any)
  default = null
}

variable "private_subnet_name" {
  description = "Name of the Private Subnets"
  type = string
  default = null
}



variable "availability_zones" {
  type        = list(string)
  description = "Availability Zones for Subnets"
  default     = null
}


