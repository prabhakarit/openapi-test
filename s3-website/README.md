
Please update website path, workflow configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 
As an AI language model, I cannot write code from scratch. However, I can provide you with a sample GitHub Actions workflow that you can use as a starting point to update your AWS S3 website and invalidate Amazon CloudFront.

Here's an example workflow:



This workflow will trigger on every push to the main branch. It will first checkout the code, then install the AWS CLI using the access key and secret access key stored in GitHub secrets. It will then sync the files in the `./dist` directory to your S3 bucket, deleting any files that no longer exist. Finally, it will create an invalidation for the CloudFront distribution with the ID `your-distribution-id`, invalidating all files.

You will need to replace `your-bucket-name` and `your-distribution-id` with your actual S3 bucket name and CloudFront distribution ID, respectively. You will also need to make sure that your AWS access key and secret access key are stored securely in GitHub secrets.

I hope this helps!