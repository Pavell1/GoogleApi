import requests
import json

url = "https://catfact.ninja/facts?max_length=100&limit=5"
result = requests.get(url)

fields = json.loads(result.text)
print(list(fields))
