/*
  declare variables
*/
variable "access_key" {
  type = string
  description = "AWS access key"
}

variable "secret_key" {
  type = string
  description = "AWS secret key"
}

variable "region" {
  type = string
  description = "AWS region"
}

variable "ami" {
  default = "ami-01154c8b2e9a14885"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "subnet_id" {
  default = "subnet-0c02fee8b7d761e52"
}

variable "vpc_security_group_ids" {
  type = list
  default = ["sg-0d259b4887cbeb0aa"]
}

variable "tags" {
  type = map
  default = {
    "Name"        = "Test"
    "Environment" = "Training"
  }
}
