import requests

city = "Seoul"
apikey = "8d32d32a2c9cd8743896215a8f38a513"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)