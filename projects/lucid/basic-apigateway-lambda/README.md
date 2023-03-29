
Please note that this is an experimental implementation. It can only provide a template as a suggestive start.
Following is documentation passed by ChatGPT : 
Here is an example Terraform code to deploy an AWS Lambda function behind an Amazon API Gateway:



This code creates an AWS Lambda function, an IAM role for the function, an Amazon API Gateway, a resource and method for the API Gateway, an integration between the API Gateway and the Lambda function, and a deployment of the API Gateway. The Lambda function is invoked when a POST request is made to the API Gateway resource.