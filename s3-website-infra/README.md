
Please update website path, workflow configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 


Here is an example Terraform script to create an AWS S3 website bucket:



This script creates an S3 bucket with the name "example-website-bucket" and sets it up as a website with an index document of "index.html" and an error document of "error.html". It also sets the bucket ACL to "public-read" and adds a bucket policy that allows public read access to all objects in the bucket. Finally, it adds a tag to the bucket with the name "Example Website Bucket".