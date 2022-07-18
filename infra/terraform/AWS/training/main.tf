/*
  values for required variables can be passed
  inline, env vars, files
*/
provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  region     = var.region
}
/*
  Create key pair for ssh
*/
module "keypair" {
  source = "mitchellh/dynamic-keys/aws"
  path   = "${path.root}/keys"
  name   = "my-key"
}

/*
  Creates ec2 instance in an existing VPC/Subnet
*/
module "server" {
  source                 = "./modules/server"
  ami                    = var.ami
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = var.vpc_security_group_ids
  key_name               = module.keypair.key_name
  private_key            = module.keypair.private_key_pem
  tags = var.tags
}

module "s3" {
  source       = "./modules/s3"
}
