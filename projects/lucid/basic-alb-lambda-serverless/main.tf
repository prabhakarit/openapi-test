
resource "aws_lb" "example" {
  name               = "example-lb"
  internal           = false
  load_balancer_type = "application"
  subnets            = ["subnet-12345678", "subnet-87654321"]
  security_groups    = ["sg-12345678"]

  tags = {
    Environment = "production"
  }
}

resource "aws_lb_target_group" "example" {
  name_prefix        = "example-tg"
  port               = 80
  protocol           = "HTTP"
  vpc_id             = "vpc-12345678"

  health_check {
    path = "/"
  }

  tags = {
    Environment = "production"
  }
}

resource "aws_lb_listener" "example" {
  load_balancer_arn = aws_lb.example.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.example.arn
  }
}

resource "aws_instance" "example" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  subnet_id     = "subnet-12345678"
  vpc_security_group_ids = ["sg-12345678"]

  tags = {
    Name = "example-instance"
  }
}

resource "aws_lb_target_group_attachment" "example" {
  target_group_arn = aws_lb_target_group.example.arn
  target_id        = aws_instance.example.id
  port             = 80
}
