
Please update website path, workflow configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 
As an AI language model, I cannot write code from scratch. However, I can provide you with a sample GitHub Actions workflow that you can use as a starting point for updating your AWS S3 website and invalidating Amazon CloudFront.

Here's an example workflow:



This workflow will trigger on every push to the main branch. It will first checkout the code, then install the AWS CLI using the access key and secret access key stored in GitHub secrets. It will then sync the files in the `public` directory to your S3 bucket, deleting any files that are no longer present. Finally, it will create an invalidation for the CloudFront distribution, which will clear the cache and ensure that the latest version of your website is served to users.

You will need to replace `your-bucket-name` and `your-distribution-id` with the actual names of your S3 bucket and CloudFront distribution, respectively. You will also need to ensure that your AWS access key and secret access key are stored securely in GitHub secrets.

I hope this helps!