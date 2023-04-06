import argparse
import csv
import openai
import os
import sys
from pathlib import Path
import shutil

select_model_babbage001 = "text-babbage-001"
select_model_chatgpt35 = "gpt-3.5-turbo"
select_model_chatgpt35_0301 = "gpt-3.5-turbo-0301"
select_model_text_ada = "text-ada-001"
select_model_code_search_ada = "code-search-ada-code-001"
select_model = select_model_chatgpt35_0301
select_temperature = 0.1

parser=argparse.ArgumentParser()
parser.add_argument('-d', '--csvFile', nargs='+', required=True, action='store', dest='csvFile', default=False, help="provide input csv file name")
parser.add_argument('-o', '--outputdir', nargs='+', required=True, action='store', dest='outputdir', default=False, help="provide output directory name")
parser.add_argument('-p', '--preference', nargs='+', required=True, action='store', dest='preference', default=False, help="provide devops preference")
args=parser.parse_args()
alldirs = args.csvFile
directory=alldirs[0]
print(f'directory = {directory}')
allPrefs = args.preference
preference=allPrefs[0]
print(f'preference = {preference}')
outputdir = args.outputdir
output=outputdir[0]
print(f'outputdir = {output}')

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
compute = ["Amazon EC2", "AWS Lambda"]
storage = ["Amazon Simple Storage Service (S3)", "Amazon RDS", "Amazon DynamoDB"]
primary_serverless = ['AWS Lambda']
secondary_serverless = ['Amazon API Gateway']

apiAccesses = []
computes = []
storages = []
primary_serverless_list = []
secondary_serverless_list = []

isComputePresent = False
isAPIAccessPresent = False
isStoragePresent = False
isPrimaryServerlessPresent = False
isSecondaryServerlessPresent = False
for resource in resources:
    if resource in compute:
        if resource in primary_serverless:
            primary_serverless_list.append(resource)
            isPrimaryServerlessPresent = True
        computes.append(resource)
        isComputePresent = True
    if resource in api_access:
        if resource in secondary_serverless:
            secondary_serverless_list.append(resource)
            isSecondaryServerlessPresent = True
        apiAccesses.append(resource)
        isAPIAccessPresent = True
    if resource in storage:
        storages.append(resource)
        isStoragePresent = True
  
# Parent Directory path
parent_dir = "../projects/lucid/"

# Path
path = os.path.join(parent_dir, output)

isExist = os.path.exists("../projects/")
if not isExist:
    os.mkdir("../projects/")

isExist = os.path.exists(parent_dir)
if not isExist:
    os.mkdir(parent_dir)

# remove folder if exists
dirpath = Path(parent_dir) / output
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

isExist = os.path.exists(path)
if not isExist:
    os.mkdir(path)

if isComputePresent == True and isAPIAccessPresent == True :
    if isPrimaryServerlessPresent == True:
        # query
        query = "serverless framework yaml code for nodejs "+ computes[0] +", " + apiAccesses[0]

        # Creates a new file
        with open(os.path.join(path, 'serverless.yml'), 'w') as fp:
            pass
        with open(os.path.join(path, 'README.md'), 'w') as fp:
            pass

        # Load your API key from an environment variable or secret management service
        openai.api_key = os.getenv("OPENAI_API_KEY")

        print("temperature = " + str(select_temperature))
        print("model = " + select_model_code_search_ada)

        completion = openai.ChatCompletion.create(
            temperature=select_temperature,
            model=select_model,
            messages=[
                {"role": "user", "content": query}
            ],
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = completion.choices[0].message.content
        #print(completion.choices[0].message.content)
        tokens = answer.split('```')
        code_answer = tokens[1]
        print(code_answer)
        # Python program to demonstrate
        # writing to file
        # Opening a file
        file1 = open(os.path.join(path, 'serverless.yml'), 'w')
        s = code_answer
        
        # Writing a string to file
        file1.write(s)
        
        # Closing file
        file1.close()

        guidance = "\nPlease note that this is an experimental implementation. It can only provide a template as a suggestive start."
        msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
        # Writing readme file
        file2 = open(os.path.join(path, 'README.md'), 'w')
        file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
        file2.close()

        # setup workflow for serverless deployment
        # query
        query = "github actions workflow code for serverless framework deployment"

        # Creates a new file
        with open(os.path.join(path, 'deployment-workflow.yml'), 'w') as fp:
            pass

        # Load your API key from an environment variable or secret management service
        openai.api_key = os.getenv("OPENAI_API_KEY")

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
        # Opening a file
        file1 = open(os.path.join(path, 'deployment-workflow.yml'), 'w')
        s = code_answer
        
        # Writing a string to file
        file1.write(s)
        
        # Closing file
        file1.close()

        if isSecondaryServerlessPresent == False:
            # query
            query = "terraform code to create " + apiAccesses[0] + " with target " + computes[0]

            # Creates a new file
            with open(os.path.join(path, 'main.tf'), 'w') as fp:
                pass

            # Load your API key from an environment variable or secret management service
            openai.api_key = os.getenv("OPENAI_API_KEY")

            completion = openai.ChatCompletion.create(
            temperature=select_temperature,
            model=select_model_code_search_ada, 
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
            file1 = open(os.path.join(path, 'main.tf'), 'w')
            s = code_answer
            
            # Writing a string to file
            file1.write(s)
            
            # Closing file
            file1.close()
    
    else :
        # argument
        query = "terraform code to deploy "+ computes[0] +" behind " + apiAccesses[0]

        # Creates a new file
        with open(os.path.join(path, 'main.tf'), 'w') as fp:
            pass
        with open(os.path.join(path, 'README.md'), 'w') as fp:
            pass

        # Load your API key from an environment variable or secret management service
        openai.api_key = os.getenv("OPENAI_API_KEY")

        completion = openai.ChatCompletion.create(
            temperature=select_temperature,
            #model="gpt-3.5-turbo", 
            model=select_model, 
            messages=[{"role": "user", "content": query}]
        )
        answer = completion.choices[0].message.content
        #print("chatgpt answer => ", answer)
        #print("code answer => ", completion.choices[0].message.content)
        tokens = answer.split('```')
        code_answer = tokens[1]
        print(code_answer)
        # Python program to demonstrate
        # writing to file
        # Opening a file
        file1 = open(os.path.join(path, 'main.tf'), 'w')
        s = code_answer
        
        # Writing a string to file
        file1.write(s)
        
        # Closing file
        file1.close()

        guidance = "\nPlease note that this is an experimental implementation. It can only provide a template as a suggestive start."
        msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
        # Writing readme file
        file2 = open(os.path.join(path, 'README.md'), 'w')
        file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
        file2.close()

if isComputePresent == True and isStoragePresent == True :
    # argument
    query = "terraform code to deploy "+ computes[0] +" with " + storages[0]

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")

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
    
    # Opening a file
    file1 = open(os.path.join(path, 'main.tf'), 'w')
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Closing file
    file1.close()

    guidance = "\nPlease note that this is an experimental implementation. It can only provide a template as a suggestive start."
    msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
    # Writing readme file
    file2 = open(os.path.join(path, 'README.md'), 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()

if isAPIAccessPresent == True and isStoragePresent == True:
    # argument
    query = "terraform code to create "+ apiAccesses[0] +" and " + storages[0]

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")

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
    
    # Opening a file
    file1 = open(os.path.join(path, 'main.tf'), 'w')
    s = code_answer
    
    # Writing a string to file
    file1.write(s)
    
    # Closing file
    file1.close()

    guidance = "\nPlease note that this is an experimental implementation. It can only provide a template as a suggestive start."
    msgFromChatGPT = "\nFollowing is documentation passed by ChatGPT : \n"
    # Writing readme file
    file2 = open(os.path.join(path, 'README.md'), 'w')
    file2.write(guidance + msgFromChatGPT + tokens[0] + tokens[2])
    file2.close()
