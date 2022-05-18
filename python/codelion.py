import requests
import json

city = "Seoul"
apikey = "8d32d32a2c9cd8743896215a8f38a513"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

# print(type(result.text))
# print(type(data))

print(data["name"],"의 날씨입니다.")
print(data["weather"])
print("Today is ",data["weather"][0]["main"])
