import requests
import os

bearer_token = os.environ.get("AAAAAAAAAAAAAAAAAAAAABBcnAEAAAAAPIkHNT2Gr%2FEqumZ3bZmOgfuVyFI%3DFIF0lcIj4SUpUnnTKIEamc0TDEveWVqpkoPg63jEIpIkReRZ3F")

url = "https://api.twitter.com/2/tweets/search/recent"

query_params = {'query': 'COVID-19'}

headers = {"Authorization": f"Bearer {bearer_token}"}

response = requests.get(url, headers=headers, params=query_params)

print(response.json())
