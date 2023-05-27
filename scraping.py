import requests

response = requests.get('https://attack.mitre.org/groups/')
print(response.text)