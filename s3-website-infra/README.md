
Please update website path, terraform configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 


Here is an example Terraform script to create an AWS S3 website bucket:



This script creates an S3 bucket named "example-website-bucket" with public read access and a website configuration that specifies "index.html" as the index document and "error.html" as the error document. It also adds a bucket policy that allows public read access to all objects in the bucket. Finally, it adds a tag to the bucket with the name "Example Website Bucket".