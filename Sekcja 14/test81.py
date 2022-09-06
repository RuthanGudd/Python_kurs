"""
pip - pip installs packages
PyPi - Python Package index 
"""

import requests

#pip install requests

response = requests.get("http://videokurs.pl")
print(response)