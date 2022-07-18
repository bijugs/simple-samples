resource "aws_s3_bucket" "student" {
  bucket_prefix = "asquareb-student-"
}

resource "aws_s3_bucket_acl" "student_bucket_acl" {
  bucket = aws_s3_bucket.student.id
  acl    = "private"
}

locals {
  policy = templatefile("${path.module}/templates/s3-policy.json.tpl", {
    bucket_name = aws_s3_bucket.student.bucket
    sid         = "MyBucketPolicy"
  })
}

data "aws_iam_user" "awsadmin" {
  user_name = "awsadmin"
}

resource "aws_iam_policy" "bucket"{
  name = "${aws_s3_bucket.student.id}-policy"
  policy = local.policy
}

resource "aws_iam_user_policy_attachment" "attach-policy" {
  user       = data.aws_iam_user.awsadmin.user_name
  policy_arn = aws_iam_policy.bucket.arn
}
