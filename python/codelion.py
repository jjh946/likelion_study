import requests

url = "http://www.icampus.skku.edu"
response = requests.get(url)

print(response.text)