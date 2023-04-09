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
        os.system("aiac " + freeTextQuery + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme-query.md' + ' --model="'+openai_model+'"')

# For plan file
planfile = args.planfile
if not (planfile is None) :
    planfilePath = str(planfile[0])
    if planfilePath != '': 
        randomised_op_folder_name = './'+str(uuid.uuid4().hex)
        isExist = os.path.exists(randomised_op_folder_name)
        if not isExist:
            os.mkdir(randomised_op_folder_name)
        print(planfilePath)
        with open(planfilePath, 'r') as fcc_file:
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
                os.system("aiac " + query + ' --output-file='+randomised_op_folder_name+'/s3-wesbite-deployment.yml ' + ' --readme-file='+randomised_op_folder_name+'/readme-pipeline.md' + ' --model="'+openai_model+'"')

# For plan file
lucidcsv = args.lucidcsv
if not (lucidcsv is None) :
    lucidcsvPath = str(lucidcsv[0])
    if lucidcsvPath != '': 
        randomised_op_folder_name = './'+str(uuid.uuid4().hex)
        isExist = os.path.exists(randomised_op_folder_name)
        if not isExist:
            os.mkdir(randomised_op_folder_name)
        print(lucidcsvPath)
        # Opening JSON file
        f = open(lucidcsvPath)
        # query generated from lucid csv
        query_increment = query_increment + 1
        os.system("aiac " + freeTextQuery + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme-lucidcsv.md' + ' --model="'+openai_model+'"')
        
        f.close()