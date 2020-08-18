resource "aws_s3_bucket" "mechris_aotd" {
  bucket = "mechris-aotd"
  acl    = "private"
}
