

As an AI language model, I cannot write code on Github. However, I can provide you with the steps to create Github actions to update AWS S3 website and invalidate Amazon CloudFront.

1. Create an AWS IAM user with S3 and CloudFront permissions.
2. Create a Github repository and add your website files to it.
3. Create a Github workflow file in the .github/workflows directory of your repository.
4. Define the workflow name, trigger, and jobs in the workflow file.
5. Add the AWS access key and secret key as Github secrets.
6. Use the AWS CLI to sync your website files to the S3 bucket.
7. Use the AWS CLI to create a CloudFront invalidation for your website.
8. Commit and push the workflow file to your Github repository.

Here is an example of a Github workflow file that updates an S3 website and invalidates CloudFront:



Make sure to replace "your-bucket-name" and "your-distribution-id" with your actual S3 bucket name and CloudFront distribution ID. Also, make sure to add your AWS access key and secret key as Github secrets.

Once you commit and push the workflow file to your Github repository, the workflow will automatically run and update your S3 website and invalidate CloudFront cache.