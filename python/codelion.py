from bs4 import BeautifulSoup
import requests

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.findAll('a'))
# file = open("daum.html","w")
# file.write(response.text)
# file.close()

# print(soup.title)
# print(soup.title.string)
# print(soup.span)
# print(soup.findAll('span'))

# html 문서에서 모든 a태그를 가져오는 코드
