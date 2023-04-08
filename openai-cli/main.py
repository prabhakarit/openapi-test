import argparse
import csv
import openai
import os
import sys
from pathlib import Path
import shutil
import os
import uuid

openai_model = "gpt-3.5-turbo-0301"

parser=argparse.ArgumentParser()
#parser.add_argument('multi_word')
parser.add_argument('-q', '--query',nargs='+', required=False, action='store', dest='query', default=False, help="provide free text query")
parser.add_argument('-p', '--planfile',nargs='+', required=False, action='store', dest='planfile', default=False, help="provide planfile to generate terraform script")
# parser.add_argument('-o', '--outputdir', nargs='+', required=False, action='store', dest='outputdir', default=False, help="provide output directory name")
# parser.add_argument('-p', '--preference', nargs='+', required=True, action='store', dest='preference', default=False, help="provide devops preference")

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
    
    os.system("aiac " + freeTextQuery + ' --output-file='+randomised_op_folder_name+'/main.tf ' + ' --readme-file='+randomised_op_folder_name+'/readme.md ' + ' --model="'+openai_model+'"')