/*
  Creates ec2 instance in an existing VPC/Subnet
*/
resource "aws_instance" "web" {
  count                  = var.num_servers
  ami                    = var.ami
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = var.vpc_security_group_ids
  key_name               = var.key_name
  tags = var.tags
  connection {
    user     = "ubuntu"
    private_key = var.private_key
    host        = self.public_ip
  }
  provisioner "remote-exec" {
    inline = [
      "sudo sed -i '/PasswordAuthentication no/c\\PasswordAuthentication yes' /etc/ssh/sshd_config",
      "sudo service ssh restart",
      "sudo useradd student${count.index} -m -d /home/student${count.index}",
      "echo 'student${count.index}:student${count.index}' | sudo chpasswd"
    ]
  }
}
