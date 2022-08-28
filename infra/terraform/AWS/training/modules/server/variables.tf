variable "ami" {}
variable "instance_type" {}
variable "subnet_id" {}
variable "vpc_security_group_ids" {
  type = list
}
variable "tags" {
  type = map
}
variable key_name {}
variable private_key {}
variable num_servers {
  type    = number
  default = 1
}
