
# Define the AWS provider
provider "aws" {
  region = "us-west-2"
}

# Create the Application Load Balancer
resource "aws_lb" "example" {
  name               = "example-lb"
  internal           = false
  load_balancer_type = "application"
  subnets            = ["subnet-12345678", "subnet-87654321"]
}

# Create the target group for the Lambda function
resource "aws_lb_target_group" "example" {
  name     = "example-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = "vpc-12345678"
}

# Create the Lambda function
resource "aws_lambda_function" "example" {
  filename         = "example.zip"
  function_name    = "example-function"
  role             = "arn:aws:iam::123456789012:role/lambda-role"
  handler          = "index.handler"
  runtime          = "nodejs14.x"
  source_code_hash = filebase64sha256("example.zip")
}

# Create the Lambda function's permission to be invoked by the ALB
resource "aws_lambda_permission" "example" {
  statement_id  = "AllowExecutionFromALB"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.example.function_name
  principal     = "elasticloadbalancing.amazonaws.com"
  source_arn    = aws_lb_target_group.example.arn
}

# Create the ALB listener rule to forward traffic to the Lambda function
resource "aws_lb_listener_rule" "example" {
  listener_arn = aws_lb.example.arn
  priority     = 100
  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.example.arn
  }
  condition {
    path_pattern {
      values = ["/example"]
    }
  }
}
