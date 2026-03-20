

# libraries and imports
import requests
from github import Github
from config import apikeys as cfg  

# Authorise using Personal Access Token 
apikey = cfg["github"]
account = Github(apikey)

# Connect to repository 
repo = account.get_repo("LDonn32/WSAA-coursework")

# modify tthe file
file_path = "assignments/andrew.txt"  
file = repo.get_contents(file_path)

# Download the file contents
response = requests.get(file.download_url)
contents = response.text

# Replace text locally
updated_contents = contents.replace("Andrew", "Laura")

# Commit the updated file back to GitHub
repo.update_file(
    path=file_path,
    message="Replaced 'Andrew' with 'Laura' for Assignment 04",
    content=updated_contents,
    sha=file.sha
)

print("The name 'Andrew' has been replaced with 'Laura'.")
