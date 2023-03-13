import openai
import os
import sys

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def terraform_s3():
    # argument
    query = "terraform main script to create AWS s3 website bucket"

    completion = openai.ChatCompletion.create(
    temperature=0.1,
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": query}]
    )
    answer = completion.choices[0].message.content
    #print(completion.choices[0].message.content)
    tokens = answer.split('```')
    code_answer = tokens[1]
    print(code_answer)
    # Python program to demonstrate
    # writing to file
    
    # Opening a file
    file1 = open('../s3-website-infra/main.tf', 'w')
    #L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Writing multiple strings
    # at a time
    #file1.writelines(L)
    
    # Closing file
    file1.close()

    guidance = "\nPlease update website path, terraform configuration in accordance to your setup.\nNote: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start."
    msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
    # Writing readme file
    file2 = open('../s3-website-infra/README.md', 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()

def action_terraform_deploy():
    # argument
    query = "create github actions workflow to run terraform init plan deploy to AWS"

    completion = openai.ChatCompletion.create(
    temperature=0.1,
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": query}]
    )
    answer = completion.choices[0].message.content
    #print(completion.choices[0].message.content)
    tokens = answer.split('```')
    code_answer = tokens[1]
    print(code_answer)
    # Python program to demonstrate
    # writing to file
    
    # Opening a file
    file1 = open('../.github/workflows/terraform-deploy.yml', 'w')
    #L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Closing file
    file1.close()

def terraform_cloudfront():
    # argument
    query = "terraform main script to create cloudfront distribution for s3 website"

    completion = openai.ChatCompletion.create(
    temperature=0.1,
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": query}]
    )
    answer = completion.choices[0].message.content
    #print(completion.choices[0].message.content)
    tokens = answer.split('```')
    code_answer = tokens[1]
    print(code_answer)
    # Python program to demonstrate
    # writing to file
    
    # Opening a file
    file1 = open('../s3-website-cloudfront/main.tf', 'w')
    #L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Writing multiple strings
    # at a time
    #file1.writelines(L)
    
    # Closing file
    file1.close()

    guidance = "\nPlease update website path, terraform configuration in accordance to your setup.\nNote: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start."
    msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
    # Writing readme file
    file2 = open('../s3-website-cloudfront/README.md', 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()

def action_deploy_s3website():
    # argument
    query = "write github actions to update to AWS s3 website and invalidate amazon cloudfront"

    completion = openai.ChatCompletion.create(
    temperature=0.1,
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": query}]
    )
    answer = completion.choices[0].message.content
    #print(completion.choices[0].message.content)
    tokens = answer.split('```')
    code_answer = tokens[1]
    print(code_answer)
    # Python program to demonstrate
    # writing to file
    
    # Opening a file
    file1 = open('../.github/workflows/s3-website.yml', 'w')
    #L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Writing multiple strings
    # at a time
    #file1.writelines(L)
    
    # Closing file
    file1.close()

    guidance = "\nPlease update website path, workflow configuration in accordance to your setup.\nNote: Please take care of security aspects of the workflow and resource setup such as S3, cloudfront. This is an experimental implementation. It can only provide a template as a suggestive start."
    msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
    # Writing readme file
    file2 = open('../s3-website/README.md', 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()

    # Writing readme file
    file3 = open('../s3-website/index.html', 'w')
    file3.write('<html><body><h2>Hello World !</h2></body></html>')
    file3.close()

# create workflow for terraform run
action_terraform_deploy()

# create terraform template for s3 website provisioning
terraform_s3()

# create terraform template for cloudfront provisioning
terraform_cloudfront()

# create workflow to deploy s3 website with cloudfront invalidation
action_deploy_s3website()