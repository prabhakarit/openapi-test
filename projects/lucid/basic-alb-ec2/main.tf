
# Define the AWS provider
provider "aws" {
  region = "us-west-2"
}

# Create a security group for the EC2 instance
resource "aws_security_group" "ec2_sg" {
  name_prefix = "ec2_sg_"
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an EC2 instance
resource "aws_instance" "ec2_instance" {
  ami = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.ec2_sg.id]
  tags = {
    Name = "EC2 Instance"
  }
}

# Create an Application Load Balancer
resource "aws_lb" "alb" {
  name = "my-alb"
  subnets = ["subnet-12345678", "subnet-87654321"]
  security_groups = [aws_security_group.alb_sg.id]
}

# Create a target group for the EC2 instance
resource "aws_lb_target_group" "ec2_target_group" {
  name_prefix = "ec2_target_group_"
  port = 80
  protocol = "HTTP"
  vpc_id = "vpc-12345678"
  health_check {
    path = "/"
    protocol = "HTTP"
  }
}

# Register the EC2 instance with the target group
resource "aws_lb_target_group_attachment" "ec2_target_attachment" {
  target_group_arn = aws_lb_target_group.ec2_target_group.arn
  target_id = aws_instance.ec2_instance.id
  port = 80
}

# Create a listener for the Application Load Balancer
resource "aws_lb_listener" "alb_listener" {
  load_balancer_arn = aws_lb.alb.arn
  port = 80
  protocol = "HTTP"
  default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.ec2_target_group.arn
  }
}
