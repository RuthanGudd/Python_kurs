"""
pip - pip installs packages
PyPi - Python Package index 
"""

import requests

path = "links.txt"

def page_access_checker(path):
    with open(path, "r", encoding = "UTF-8") as file:
        with open("result.txt", "w") as file2:
            links = file.read().splitlines()
            for line in links:
                response = requests.get(line)
                if response.status_code == 200:
                    file2.write("Working        " + line + "\n")
                else:
                    file2.write("Not Working    " + line + "\n")

page_access_checker(path)