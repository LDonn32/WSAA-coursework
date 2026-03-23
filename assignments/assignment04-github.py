

# libraries and imports
import requests
import re
from config import apikeys as cfg
from github import Github, Auth

# Authorise using Personal Access Token 
apikey = cfg["github"]
auth = Auth.Token(apikey)
account = Github(auth=auth)

# Connect to repository 
repo = account.get_repo("LDonn32/-WSAA-coursework")

# modify tthe file
file_path = "assignments/andrew.txt"  
file = repo.get_contents(file_path)

# Download the file contents
response = requests.get(file.download_url)
contents = response.text

# Replace text locally (case-insensitive)
updated_contents = re.sub(r'Andrew', 'Laura', contents, flags=re.IGNORECASE)

# Commit the updated file back to GitHub
repo.update_file(
    path=file_path,
    message="Replaced 'Andrew' with 'Laura' for Assignment 04",
    content=updated_contents,
    sha=file.sha
)

print("The name 'Andrew' has been replaced with 'Laura'.")
