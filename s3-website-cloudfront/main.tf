
# Define the AWS provider
provider "aws" {
  region = "us-east-1"
}

# Define the S3 bucket for the website
resource "aws_s3_bucket" "website_bucket" {
  bucket = "example-website-bucket"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

# Define the CloudFront distribution
resource "aws_cloudfront_distribution" "website_distribution" {
  origin {
    domain_name = aws_s3_bucket.website_bucket.website_endpoint
    origin_id   = "S3-${aws_s3_bucket.website_bucket.id}"
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${aws_s3_bucket.website_bucket.id}"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  price_class = "PriceClass_100"

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}
