import requests
from send_email import send_email

api_key = "66f46eff71c54001a25699a975669917"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "sortBy=publishedAt&apiKey=66f46eff71c54001a25699"
       "a975669917")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

body = ""

# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
