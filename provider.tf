terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 5.0"
    }
  }
}

#CONFIGURE THE AWS PROVIDER
provider "aws" {
  region = "ap-south-1"   #change as per your requirement
}