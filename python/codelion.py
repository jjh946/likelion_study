from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('a','link_favorsch')

print(datetime.today())

for result in results:
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1