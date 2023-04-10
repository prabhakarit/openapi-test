import argparse
import csv
import openai
import os
import sys
from pathlib import Path
import shutil
import os
import uuid
import json

openai_model = "gpt-3.5-turbo-0301"

query_increment = 0

parser=argparse.ArgumentParser()
#parser.add_argument('multi_word')
parser.add_argument('-q', '--query',nargs='+', required=False, action='store', dest='query', default=None, help="provide free text query")
parser.add_argument('-p', '--planfile',nargs='+', required=False, action='store', dest='planfile', default=None, help="provide plan file path to generate provisioning & pipeline script")
parser.add_argument('-lc', '--lucidcsv',nargs='+', required=False, action='store', dest='lucidcsv', default=None, help="provide lucid csv file path to generate provisioning & pipeline script")

args=parser.parse_args()

# For Free Query
queryText = args.query
if not (queryText is None) :
    freeTextQuery=str(queryText[0])
    if freeTextQuery != '': 
        randomised_op_folder_name = './'+str(uuid.uuid4().hex)
        isExist = os.path.exists(randomised_op_folder_name)
        if not isExist:
            os.mkdir(randomised_op_folder_name)
        # print(freeTextQuery)
        query_increment = query_increment + 1
        extension = '.tf'
        if 'terraform' in freeTextQuery:
            extension = '.tf'
        if 'python' in freeTextQuery:
            extension = '.py'
        if 'java' in freeTextQuery:
            extension = '.java'
        if 'nodejs' in freeTextQuery:
            extension = '.js'
        if 'javascript' in freeTextQuery:
            extension = '.js'
        if 'github actions' in freeTextQuery:
            extension = '.yml'
        os.system("aiac " + freeTextQuery + ' --output-file='+randomised_op_folder_name+'/main.'+ extension +' --readme-file='+randomised_op_folder_name+'/readme-query.md' + ' --model="'+openai_model+'"')

# For plan file
planfile = args.planfile
if not (planfile is None) :
    planfilePath = str(planfile[0])
    if planfilePath != '': 
        print(planfilePath)
        with open(planfilePath, 'r') as fcc_file:
            randomised_op_folder_name = './'+str(uuid.uuid4().hex)
            isExist = os.path.exists(randomised_op_folder_name)
            if not isExist:
                os.mkdir(randomised_op_folder_name)
            # Opening JSON file
            fcc_data = json.load(fcc_file)
            # decide how to build query
            if "provision" in fcc_data :
                if "provider" in fcc_data["provision"] :
                    cloudprovider = fcc_data["provision"]["cloudprovider"][0]
                    resources = ""
                    for resource in fcc_data["provision"]["resources"]:
                        resources = resources + ", " + cloudprovider + " " + resource
                    query = "get " + fcc_data["provision"]["provider"]["shortlisted"][0] + " for " + resources
                    print("Query for provisioning => " + query)
                    # query generated from plan file
                    query_increment = query_increment + 1
                    os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme-provision.md' + ' --model="'+openai_model+'"')
            if "pipeline" in fcc_data :
                pipeline = fcc_data["pipeline"]["pipeline"]
                cloudprovider = fcc_data["pipeline"]["cloudprovider"][0]
                resource = fcc_data["pipeline"]["resource"][0]
                query = "get " + pipeline + " for deploying " + cloudprovider + " " + resource
                print("Query for pipeline => " + query)
                query_increment = query_increment + 1
                os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/pipeline.yml ' + ' --readme-file='+randomised_op_folder_name+'/readme-pipeline.md' + ' --model="'+openai_model+'"')

# For plan file
lucidcsvList = args.lucidcsv
if not (lucidcsvList is None) :
    lucidcsvPath = str(lucidcsvList[0])
    resources = []
    if lucidcsvPath != '': 
        with open(lucidcsvPath, 'r') as fcc_file:
            randomised_op_folder_name = './'+str(uuid.uuid4().hex)
            isExist = os.path.exists(randomised_op_folder_name)
            if not isExist:
                os.mkdir(randomised_op_folder_name)
            print(lucidcsvPath)
            # parse CSV
            csv_reader = csv.reader(fcc_file, delimiter=',')
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
            # for compute and api access
            if isComputePresent == True and isAPIAccessPresent == True :
                if isPrimaryServerlessPresent == True:
                    # query
                    query = "get serverless framework yaml for nodejs "+ computes[0] +", " + apiAccesses[0]
                    os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/serverless.yml ' + ' --readme-file='+randomised_op_folder_name+'/readme-serverless.md' + ' --model="'+openai_model+'"')

                    # setup workflow for serverless deployment
                    # query
                    query = "get github actions workflow for serverless framework deployment"
                    os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/pipeline.yml ' + ' --readme-file='+randomised_op_folder_name+'/readme-pipeline.md' + ' --model="'+openai_model+'"')

                    if isSecondaryServerlessPresent == False:
                        # query
                        query = "get terraform for " + apiAccesses[0] + " with target " + computes[0]
                        os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme-provision.md' + ' --model="'+openai_model+'"')

                else :
                    # argument
                    query = "get terraform for "+ computes[0] +" behind " + apiAccesses[0]
                    os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme-provision.md' + ' --model="'+openai_model+'"')

            if isComputePresent == True and isStoragePresent == True :
                # argument
                query = "get terraform for "+ computes[0] +" with " + storages[0]
                os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme-provision.md' + ' --model="'+openai_model+'"')

            if isAPIAccessPresent == True and isStoragePresent == True:
                # argument
                query = "get terraform for "+ apiAccesses[0] +" and " + storages[0]
                os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme-provision.md' + ' --model="'+openai_model+'"')  