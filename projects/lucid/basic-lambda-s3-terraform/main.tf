
# Define the provider
provider "aws" {
  region = "us-west-2"
}

# Define the S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
}

# Define the Lambda function
resource "aws_lambda_function" "my_lambda" {
  function_name = "my-lambda"
  handler = "index.handler"
  runtime = "nodejs14.x"
  role = aws_iam_role.lambda.arn
  filename = "lambda.zip"
}

# Define the IAM role for the Lambda function
resource "aws_iam_role" "lambda" {
  name = "lambda-role"
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

# Define the IAM policy for the Lambda function
resource "aws_iam_policy" "lambda" {
  name = "lambda-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Effect = "Allow"
        Resource = [
          "${aws_s3_bucket.my_bucket.arn}/*"
        ]
      }
    ]
  })
}

# Attach the IAM policy to the IAM role
resource "aws_iam_role_policy_attachment" "lambda" {
  policy_arn = aws_iam_policy.lambda.arn
  role = aws_iam_role.lambda.name
}

# Define the S3 bucket notification configuration
resource "aws_s3_bucket_notification" "my_bucket_notification" {
  bucket = aws_s3_bucket.my_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.my_lambda.arn
    events = [
      "s3:ObjectCreated:*"
    ]
    filter_prefix = "uploads/"
  }
}
