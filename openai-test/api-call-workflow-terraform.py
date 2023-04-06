import openai
import os
import sys

select_model_babbage001 = "text-babbage-001"
select_model =select_model_babbage001
select_temperature = 0.1

# argument
query = "create github actions workflow to run terraform init plan deploy to AWS"

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
file1 = open('../.github/workflows/terraform-deploy.yml', 'w')
#L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = code_answer
 
# Writing a string to file
file1.write(s)
 
# Writing multiple strings
# at a time
#file1.writelines(L)
 
# Closing file
file1.close()