region = "ap-south-1"
cidr_block = "10.5.0.0/16"

vpc_tags= {
    Name = "Ronak_VPC"
    Owner   = "ronak.bali@cloudeq.com"
    product = "RONAK_TESTING_QREST"
    }


public_subnet_cidrs = ["10.5.1.0/24"]
public_subnet_name = "Ronak_Public_Subnet"

private_subnet_cidrs = ["10.5.2.0/24","10.5.3.0/24"]
private_subnet_name = "Ronak_Private_Subnet"

availability_zones = ["ap-south-1a", "ap-south-1b"]