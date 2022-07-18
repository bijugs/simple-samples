{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "${sid}",
      "Action": [
        "s3:CreateBucket",
        "s3:DeleteBucket",
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:ListObjects"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::${bucket_name}"
    }
  ]
}
