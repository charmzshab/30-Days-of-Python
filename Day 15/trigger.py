import requests

ngrok_url = "http://69fa2dffc242.ngrok.io"
endpoint = f"{ngrok_url}/box-office-mojo-scraper"

r = requests.post(endpoint, json={})
print(r.json()["data"])
