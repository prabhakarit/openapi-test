
Please update website path, terraform configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 


Here is an example Terraform script to create a CloudFront distribution for an S3 website:



This script creates an S3 bucket for the website, an origin access identity for the bucket, and a CloudFront distribution that points to the S3 bucket. The distribution is configured to use HTTPS and to redirect HTTP requests to HTTPS. It also sets up caching and allows access from any location. Finally, it sets up aliases for the website.