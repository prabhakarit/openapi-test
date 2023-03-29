import argparse
import csv
import openai
import os
import sys

parser=argparse.ArgumentParser()
parser.add_argument('-d', '--directory', nargs='+', required=True, action='store', dest='directory', default=False, help="provide directory name")
parser.add_argument('-p', '--preference', nargs='+', required=True, action='store', dest='preference', default='terraform', choices=['terraform', 'serverless'], help="provide devops preference")
args=parser.parse_args()
alldirs = args.directory
directory=alldirs[0]
print(f'directory = {directory}')
allPrefs = args.preference
preference=allPrefs[0]
print(f'preference = {preference}')

resources = []

# create map object


with open('../lucid-files/'+directory+'.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[1] == "Document" or row[1] == "Page" or row[1] == "Line":
                print(f'skipping for {row[1]}')
                continue
            else:
                resources.append(row[1])
                print(f'added {row[1]} to resource')
            line_count += 1
    print(f'Processed {line_count} lines.')
    print(f'Resources to be processed {resources}')

api_access = ['Application Load Balancer',  'Amazon API Gateway']
compute = ["EC2", "AWS Lambda"]
storage = ["S3", "RDS"]

apiAccesses = []
computes = []
storages = []

isComputePresent = False
isAPIAccessPresent = False
isStoragePresent = False
for resource in resources:
    if resource == "AWS Lambda" or resource == "EC2":
        computes.append(resource)
        isComputePresent = True
    if resource == "Application Load Balancer" or resource == "Amazon API Gateway":
        apiAccesses.append(resource)
        isAPIAccessPresent = True
    if resource == "S3" or resource == "RDS":
        storages.append(resource)
        isStoragePresent = True
  
# Parent Directory path
parent_dir = "../projects/lucid/"

# Path
path = os.path.join(parent_dir, directory)
isExist = os.path.exists(parent_dir)
if not isExist:
    os.mkdir(parent_dir)
isExist = os.path.exists(path)
if not isExist:
    os.mkdir(path)

if isComputePresent == True and isAPIAccessPresent == True:
    # argument
    query = "terraform code to deploy "+ computes[0] +" behind " + apiAccesses[0]

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")

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
    file1 = open(os.path.join(directory, 'main.tf'), 'w')
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Writing multiple strings
    # at a time
    #file1.writelines(L)
    
    # Closing file
    file1.close()

    guidance = "\nPlease note that this is an experimental implementation. It can only provide a template as a suggestive start."
    msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
    # Writing readme file
    file2 = open(os.path.join(directory, 'README.md'), 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()
if isComputePresent == True and isStoragePresent == True:
    # argument
    query = "terraform code to deploy "+ computes[0] +" with " + storages[0]

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")

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
    file1 = open(os.path.join(directory, 'main.tf'), 'w')
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Writing multiple strings
    # at a time
    #file1.writelines(L)
    
    # Closing file
    file1.close()

    guidance = "\nPlease note that this is an experimental implementation. It can only provide a template as a suggestive start."
    msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
    # Writing readme file
    file2 = open(os.path.join(directory, 'README.md'), 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()

