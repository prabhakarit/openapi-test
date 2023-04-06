import argparse
import openai
import os
import sys

select_model_chatgpt35 = "gpt-3.5-turbo"
select_model_babbage001 = "text-babbage-001"
select_model = select_model_chatgpt35
select_temperature = 0.1

parser=argparse.ArgumentParser()
parser.add_argument('-d', '--directory', nargs='+', required=True, action='store', dest='directory', default=False, help="provide directory name")
args=parser.parse_args()
alldirs = args.directory
directory=alldirs[0]
print(f'directory = {directory}')

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


def terraform_s3():
    # argument
    query = "terraform main script to create AWS s3 website bucket"

    completion = openai.ChatCompletion.create(
    temperature=select_temperature,
    model=select_model, 
    messages=[{"role": "user", "content": query}]
    )
    answer = completion.choices[0].message.content
    #print(completion.choices[0].message.content)
    tokens = answer.split('```')
    code_answer = tokens[1]
    print(code_answer)
    # Python program to demonstrate
    # writing to file

    path = "../projects/"+directory+"/"
    project_path = path+"s3-website-infra/"

    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
    isExist = os.path.exists(project_path)
    if not isExist:
        os.mkdir(project_path)
    # Creates a new file
    with open(os.path.join(project_path, 'main.tf'), 'w') as fp:
        pass
    with open(os.path.join(project_path, 'README.md'), 'w') as fp:
        pass
    # Opening a file
    file1 = open(project_path+'main.tf', 'w')
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
    file2 = open(project_path + 'README.md', 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()

# create terraform template for s3 website provisioning
terraform_s3()