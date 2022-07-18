/*
  Outputs the public ip of instance
*/
output "public_ip" {
  value = aws_instance.web[*].public_ip
}

/*
  Outputs the DNS entry for the ec2 instance
*/
output "public_dns" {
  value = aws_instance.web[*].public_dns
}
