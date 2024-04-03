import requests
import json

# Set up the access token and search query
access_token = "EAATqD7b8UdYBACNeU10MJSeOMLgFm8GZB7mn60ZC0gor53tm15Abk3ZCEsbI73le5Ia1EqGzZATV6AjUrrQdogBmQOnjB3WziMlog7FgWU4POTnGbZBinDdry7iOKgFxhB8Nnhkhs2PMX0tF1exhRLEyivuZA1j6whPmlX0bmgX3FE0oZBh8mbqGW88Cn66k2nfuZCpowLBJqQkzhmhgoLjemYln3aZB6kYdB4RvZBPAd428DeLAngWSZC7"
search_query = "covid 19"

# Make a request to the Facebook Graph API to search for posts
url = f"https://graph.facebook.com/v12.0/search?q={search_query}&type=post&access_token={access_token}&since=2020-01-01&until=2020-12-31"
response = requests.get(url)

# Parse the JSON response and extract the post IDs
data = json.loads(response.text)
post_ids = [post["id"] for post in data["data"]]

# Print the post IDs
print(post_ids)
