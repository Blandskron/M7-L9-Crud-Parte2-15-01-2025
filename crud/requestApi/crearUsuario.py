import requests
import json

url = "http://127.0.0.1:8000/api/users/"

payload = json.dumps({
  "username": "Aldo2",
  "email": "aldo2@gmail.com",
  "first_name": "Aldo2",
  "last_name": "Frez2"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'sessionid': '{{apiKey}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
