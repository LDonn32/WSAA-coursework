# Assignment 02 - carddraw.py: Card Draw Game

This program interacts with the Deck of Cards API to simulate drawing a 5‑card poker hand.
After drawing the cards, the script reads the hand and congratulates the user if they achieve:

A Pair

A Three‑of‑a‑Kind

A Straight

A Flush

If none of these combinations appear, the program prints an encouraging “try again” message.

__What the program does:__

Calls a public REST API

Parses JSON responses

Works with lists and dictionaries

Using Python’s Counter for frequency analysis


__References:__

[Deck of Cards API Documentation](https://deckofcardsapi.com/)

[Python Requests Library](https://requests.readthedocs.io/)

[Python Collections — Counter](https://docs.python.org/3/library/collections.html#collections.Counter) 


__Notes:__

The script is self‑contained and requires only the requests library


# Assignment 03-cso.py: CSO API Dataset Downloader

This program retrieves data from the Central Statistics Office PxStat API and saves the full dataset to a local JSON file.


__What the program does:__

Connects to the CSO PxStat REST API

Downloads the full dataset for cube FIQ02

Saves the response to a file called cso.json

Provides a simple example of working with public APIs in Python

__Files Included:__

1. assignment03-cso.py

The base code script in a python file (No comments).

2. assignment03-cso.ipynb

The script in a Jupyter notebook version, with added notes and comments.

3. cso.json

The data returned.

__References:__

[CSO PxStat API Documentation](https://ws.cso.ie/public/api.restful)

[JSON‑Stat Format Specification](https://json-stat.org)

[Python Requests Documentation](https://requests.readthedocs.io)

Adapted code based of WSAA's Week 3 course



# Assignment 04-github.py: GitHub API File Update Script

This assignment demonstrates how to authenticate with the GitHub API, read a file from a repository, update it, and push the updated file back to GitHub.

The script uses PyGithub, requests, and a config file to securely manage API credentials.

__What the program does:__

Reads a file called andrew.txt from a GitHub repository

Replaces all instances of "Andrew" with "laura"

Commits and pushes the updated file back to the repository


__Files Included:__
1. assignment04-github.py
The main Python script that:

Authenticates with GitHub using a Fine‑Grained Personal Access Token

Connects to the repository LDonn32/WSAA-coursework

Reads the file assignments/andrew.txt

Replaces "Andrew" with "Laura"

Commits and pushes the updated file back to GitHub

2. config.py
Stores the GitHub token securely:

`python`
`config = {`
    `"GITHUB_TOKEN": "YOUR_TOKEN_HERE"`
`}`
This file is not committed to GitHub for security reasons, see notes for more details.


__Notes:__
config.py must be excluded from pushes to the repository. 

Add the line to the .gitignore file:

`# my configuration files `
`config.py`

The script assumes the file exists at:
assignments/andrew.txt

The token must be regenerated if permissions are changed. The permission for contents needs to allow read and write to change the file, otherwise an error 403: Resource not accessible by personal access token will occur. 

The script prints the original content and GitHub’s response for verification


__References:__

[GitHub REST API Documentation](https://docs.github.com/en/rest/repos/contents)

[StackOverflow for best practices for API keys](https://stackoverflow.com/questions/56995350/best-practices-python-where-to-store-api-keys-tokens)

[Pyhithub for sample code examples](https://pygithub.readthedocs.io/en/latest/examples/Repository.html)

Adapted code based of WSAA's Week 4 Labs



