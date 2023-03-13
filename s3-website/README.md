
Please update website path, workflow configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 


As an AI language model, I cannot write code on Github. However, I can provide you with the steps to create Github actions to update AWS S3 website and invalidate Amazon CloudFront.

1. Create an AWS IAM user with S3 and CloudFront permissions.
2. Create an S3 bucket and enable static website hosting.
3. Create a CloudFront distribution and configure it to use the S3 bucket as the origin.
4. Add the AWS access key and secret key as Github secrets.
5. Create a Github action that runs on push to the main branch.
6. Use the AWS CLI to sync the local files with the S3 bucket.
7. Use the AWS CLI to create an invalidation for the CloudFront distribution.

Here is an example Github action YAML file:



Replace `your-bucket-name` and `your-distribution-id` with your S3 bucket name and CloudFront distribution ID, respectively.

Note: Make sure to secure your AWS access keys and secret keys by using Github secrets.