provider "aws" {
  region = var.region
}


resource "aws_vpc" "main" {
    cidr_block = var.cidr_block
    tags = var.vpc_tags
}


resource "aws_subnet" "public_subnets" {
    count      = length(var.public_subnet_cidrs)
    vpc_id     = aws_vpc.main.id
    cidr_block = element(var.public_subnet_cidrs, count.index)
    availability_zone = element(var.availability_zones, count.index)
    tags = merge(var.public_subnet_tags,{Name = "${var.public_subnet_name}-${count.index + 1}"})
}


resource "aws_subnet" "private_subnets" {
    count      = length(var.private_subnet_cidrs)
    vpc_id     = aws_vpc.main.id
    cidr_block = element(var.private_subnet_cidrs, count.index)
    availability_zone = element(var.availability_zones, count.index)
    tags = merge(var.private_subnet_tags,{Name = "${var.private_subnet_name}-${count.index + 1}"})
    
}
