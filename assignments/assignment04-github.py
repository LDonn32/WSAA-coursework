


# Import libraries -  PyGithub and a config.py file for the token.

from github import Github, Auth
from config import config as cfg
import requests


# Load GitHub token from config.py

apikey = cfg["GITHUB_TOKEN"]

# authenticate with GitHub API
auth = Auth.Token(apikey)
g = Github(auth=auth)


# Connect to repository

repo = g.get_repo("LDonn32/WSAA-coursework")

# test connection
print("Connected to:", repo.clone_url)


# Get the file contents from the repo

fileInfo = repo.get_contents("assignments/andrew.txt")

# get the download URL so we can read the file text
urlOfFile = fileInfo.download_url

# read the file text
response = requests.get(urlOfFile)
contentOfFile = response.text
print("Original file content:")
print(contentOfFile)


# Replace "Andrew" with "laura"

new_content = contentOfFile.replace("Andrew", "laura")


# Update the file in the repository

gitHubResponse = repo.update_file(
    fileInfo.path,
    "Updated by program: replaced Andrew with laura",
    new_content,
    fileInfo.sha
)

print("Update complete:")
print(gitHubResponse)











































































































