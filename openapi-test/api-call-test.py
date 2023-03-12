import openai
import os
import sys

# argument
query = "write github actions to update to AWS s3 website and invalidate amazon cloudfront"
# if query:
#     # nothing to do
#     print('query received = ', query)
# else:
#     query = "write github actions to update to AWS s3 website and invalidate amazon cloudfront"
#     print('query default = ', query)

# project = sys.argv[2]
 
# Arguments passed
# print("\nName of Python script:", sys.argv[0])

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
file1 = open('../../.github/workflows/s3-website.yml', 'w')
#L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = code_answer
 
# Writing a string to file
file1.write(s)
 
# Writing multiple strings
# at a time
#file1.writelines(L)
 
# Closing file
file1.close()
 
# Writing readme file
file2 = open('../../s3-website/README.md', 'w')
file2.write(tokens[0] + tokens[2])
file2.close()