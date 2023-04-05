import openai
import os
import sys

select_model = "text-ada-001"
select_temperature = 0.1

# argument
query = "terraform main script to create AWS s3 website bucket"

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