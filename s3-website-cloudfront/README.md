
Please update website path, terraform configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 


Here is an example Terraform script to create a CloudFront distribution for an S3 website:



This script creates an S3 bucket for the website, an origin access identity for CloudFront to access the S3 bucket, and a CloudFront distribution that uses the S3 bucket as its origin. The default cache behavior is set to cache GET and HEAD requests for 1 hour, and to redirect HTTP requests to HTTPS. The distribution is set to use the CloudFront default SSL certificate, and is tagged with an "Environment" tag.