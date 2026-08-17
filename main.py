import requests
from send_email import send_email
import os


topic = "tesla"

api_key = os.getenv("apakey")

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt"
       f"&apiKey={api_key}" 
       "&language=en")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

body = "Subject: Today's news" + "\n"

# Access the article titles and description
for article in content["articles"][:20]:
    print(article["title"])
    if article["title"] and article["description"] and article["url"]:
        body = body + article["title"] + "\n" + article["description"] +"\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
