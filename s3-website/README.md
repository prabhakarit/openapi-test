

As an AI language model, I cannot write code on Github. However, I can provide you with the steps to update AWS S3 website and invalidate Amazon CloudFront using Github Actions.

1. Create an AWS IAM user with S3 and CloudFront access.
2. Add the AWS access key and secret key as Github secrets.
3. Create a Github Actions workflow file in your repository.
4. Use the AWS CLI to sync your local files with the S3 bucket.
5. Use the AWS CLI to create a CloudFront invalidation.

Here is an example Github Actions workflow file:



Replace `your-bucket-name` and `your-distribution-id` with your S3 bucket name and CloudFront distribution ID, respectively.

This workflow will run on every push to the `main` branch. It will install the AWS CLI, sync your local files with the S3 bucket, and create a CloudFront invalidation. The AWS access key and secret key are retrieved from Github secrets.