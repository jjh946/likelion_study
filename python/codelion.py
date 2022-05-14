import requests

url = "http://www.daum.net"
response = requests.get(url)

print(response.text)