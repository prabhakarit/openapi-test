
# Define the AWS provider
provider "aws" {
  region = "us-west-2"
}

# Create a security group for the EC2 instance
resource "aws_security_group" "ec2_sg" {
  name_prefix = "ec2_sg_"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an EC2 instance
resource "aws_instance" "ec2_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = "subnet-12345678"
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello World" > index.html
              nohup python -m SimpleHTTPServer 80 &
              EOF
}

# Create an Application Load Balancer
resource "aws_lb" "alb" {
  name               = "my-alb"
  internal           = false
  load_balancer_type = "application"
  subnets            = ["subnet-12345678", "subnet-87654321"]
}

# Create a target group for the EC2 instance
resource "aws_lb_target_group" "tg" {
  name_prefix      = "tg_"
  port             = 80
  protocol         = "HTTP"
  target_type      = "instance"
  vpc_id           = "vpc-12345678"
  health_check {
    healthy_threshold   = 2
    interval            = 30
    protocol            = "HTTP"
    timeout             = 5
    unhealthy_threshold = 2
  }
}

# Register the EC2 instance with the target group
resource "aws_lb_target_group_attachment" "tg_attachment" {
  target_group_arn = aws_lb_target_group.tg.arn
  target_id        = aws_instance.ec2_instance.id
  port             = 80
}

# Create a listener for the Application Load Balancer
resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_lb.alb.arn
  port              = 80
  protocol          = "HTTP"
  default_action {
    target_group_arn = aws_lb_target_group.tg.arn
    type             = "forward"
  }
}
