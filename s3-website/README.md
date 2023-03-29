
Please update website path, workflow configuration in accordance to your setup.
Note: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 
As an AI language model, I cannot write code on my own. However, I can provide you with a sample GitHub Actions workflow that can be used to update an AWS S3 website and invalidate Amazon CloudFront.

Here is a sample workflow:



This workflow will trigger on every push to the main branch. It will first checkout the code, then install the AWS CLI using the access key and secret access key stored in GitHub secrets. It will then sync the files in the current directory to the S3 bucket specified in the `s3://your-bucket-name` parameter, and delete any files in the bucket that are not present in the current directory. Finally, it will invalidate the CloudFront cache for the distribution specified in the `your-distribution-id` parameter.

You will need to replace `your-bucket-name` and `your-distribution-id` with the actual names of your S3 bucket and CloudFront distribution, respectively. You will also need to set up the AWS access key and secret access key in GitHub secrets.

I hope this helps!