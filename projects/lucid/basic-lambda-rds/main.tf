
# Define provider
provider "aws" {
  region = "us-east-1"
}

# Create VPC
resource "aws_vpc" "example_vpc" {
  cidr_block = "10.0.0.0/16"
}

# Create subnet
resource "aws_subnet" "example_subnet" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.1.0/24"
}

# Create security group for Lambda function
resource "aws_security_group" "lambda_sg" {
  name_prefix = "lambda_sg_"
  vpc_id      = aws_vpc.example_vpc.id

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create security group for RDS database
resource "aws_security_group" "rds_sg" {
  name_prefix = "rds_sg_"
  vpc_id      = aws_vpc.example_vpc.id

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["10.0.1.0/24"]
  }
}

# Create RDS database
resource "aws_db_instance" "example_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  name                 = "example_db"
  username             = "admin"
  password             = "password"
  db_subnet_group_name = aws_db_subnet_group.example_db_subnet_group.name
  vpc_security_group_ids = [
    aws_security_group.rds_sg.id,
  ]
}

# Create RDS database subnet group
resource "aws_db_subnet_group" "example_db_subnet_group" {
  name       = "example_db_subnet_group"
  subnet_ids = [
    aws_subnet.example_subnet.id,
  ]
}

# Create Lambda function
resource "aws_lambda_function" "example_lambda" {
  filename         = "example_lambda.zip"
  function_name    = "example_lambda"
  role             = aws_iam_role.example_lambda_role.arn
  handler          = "example_lambda.handler"
  runtime          = "nodejs12.x"
  vpc_config {
    subnet_ids         = [aws_subnet.example_subnet.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
  environment {
    variables = {
      DB_HOST     = aws_db_instance.example_db.address
      DB_USERNAME = aws_db_instance.example_db.username
      DB_PASSWORD = aws_db_instance.example_db.password
      DB_NAME     = aws_db_instance.example_db.name
    }
  }
}

# Create IAM role for Lambda function
resource "aws_iam_role" "example_lambda_role" {
  name = "example_lambda_role"

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

# Attach policy to IAM role
resource "aws_iam_role_policy_attachment" "example_lambda_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonRDSFullAccess"
  role       = aws_iam_role.example_lambda_role.name
}
