import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net/"
response = requests.get(url)
# print(response.text)

print(BeautifulSoup(response.text, 'html.parser'))