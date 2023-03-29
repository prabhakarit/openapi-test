
provider "aws" {
  region = "us-west-2"
}

resource "aws_lambda_function" "example_lambda" {
  filename         = "example_lambda.zip"
  function_name    = "example_lambda"
  role             = aws_iam_role.lambda_role.arn
  handler          = "example_lambda.handler"
  runtime          = "nodejs12.x"
  source_code_hash = filebase64sha256("example_lambda.zip")

  environment {
    variables = {
      BUCKET_NAME = aws_s3_bucket.example_bucket.id
    }
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
  role       = aws_iam_role.lambda_role.name
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "example-bucket"
}

resource "aws_s3_bucket_object" "example_object" {
  bucket = aws_s3_bucket.example_bucket.id
  key    = "example_object.txt"
  source = "example_object.txt"
}
