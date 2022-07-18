output "public_ip" {
  value = module.server.public_ip
}

output "public_dns" {
  value = module.server.public_dns
}

output "s3_policy" {
  value = module.s3.iam_policy
}

output "s3_bucket" {
  value = module.s3.bucket
}
