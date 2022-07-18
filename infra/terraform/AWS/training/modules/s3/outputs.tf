output "iam_policy" {
  value = local.policy
}

output "bucket" {
  value = aws_s3_bucket.student.bucket
}
