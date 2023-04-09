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

parser=argparse.ArgumentParser()
#parser.add_argument('multi_word')
parser.add_argument('-q', '--query',nargs='+', required=False, action='store', dest='query', default=False, help="provide free text query")
parser.add_argument('-p', '--planfile',nargs='+', required=False, action='store', dest='planfile', default=False, help="provide plan file path to generate provisioning & pipeline script")
parser.add_argument('-lc', '--lucidcsv',nargs='+', required=False, action='store', dest='lucidcsv', default=False, help="provide lucid csv file path to generate provisioning & pipeline script")

args=parser.parse_args()

# For Free Query
queryText = args.query
freeTextQuery=queryText[0]

if freeTextQuery != '': 
    randomised_op_folder_name = './'+str(uuid.uuid4().hex)
    isExist = os.path.exists(randomised_op_folder_name)
    if not isExist:
        os.mkdir(randomised_op_folder_name)
    # print(freeTextQuery)
    os.system("aiac " + freeTextQuery + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme.md ' + ' --model="'+openai_model+'"')

# For plan file
planfile = args.planfile
planfilePath = planfile[0]

if planfilePath != '': 
    randomised_op_folder_name = './'+str(uuid.uuid4().hex)
    isExist = os.path.exists(randomised_op_folder_name)
    if not isExist:
        os.mkdir(randomised_op_folder_name)
    print(planfilePath)
    with open('fcc.json', 'r') as fcc_file:
        # Opening JSON file
        fcc_data = json.load(fcc_file)
        # decide how to build query
        if fcc_data["provision"] :
            # query generated from plan file
            os.system("aiac " + freeTextQuery + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme.md ' + ' --model="'+openai_model+'"')
        

# For plan file
lucidcsv = args.lucidcsv
lucidcsvPath = lucidcsv[0]

if lucidcsvPath != '': 
    randomised_op_folder_name = './'+str(uuid.uuid4().hex)
    isExist = os.path.exists(randomised_op_folder_name)
    if not isExist:
        os.mkdir(randomised_op_folder_name)
    print(lucidcsvPath)
    # Opening JSON file
    f = open(lucidcsvPath)
    # query generated from lucid csv
    os.system("aiac " + freeTextQuery + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme.md ' + ' --model="'+openai_model+'"')
    
    f.close()