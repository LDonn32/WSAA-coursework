
# libraries
import requests

# API key and library for GitHub
from config import apikeys as cfg
from github import Github

# import API key from config file
apikey=cfg["github"]

# provide authorisation and access private repository
account=Github(apikey)
repo=account.get_repo('LDonn32/aprivateone')

# retrieve text file we want to use
file_path="andrew.txt"
file=repo.get_contents(file_path)
url=file.download_url
response=requests.get(url)
contents=response.text

# put contents of text file into local file
replacement_text='replace_text.txt'
with open (replacement_text,'w') as r_file:
    r_file.write(contents)

# replace the name Andrew with  Laura
with open (replacement_text, 'r') as new_r_file:
    new_data=new_r_file.read().replace("Andrew", "Laura")

# add the changes to the file
with open (replacement_text, 'w') as text:
    new_text=text.write(new_data)

# commit and push the changed file
repo.update_file(
    path=file_path,
    message='Replaced Andrew with Laura',
    content=new_text,
    sha=file.sha
    )

print("The name Andrew has been replaced with the name Laura")































