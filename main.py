import requests
from send_email import send_email

topic = "tesla"

api_key = "66f46eff71c54001a25699a975669917"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt"
       "&apiKey=66f46eff71c54001a25699a975669917" 
       "&language=en")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

body = ""

# Access the article titles and description
for article in content["articles"][:20]:
    print(article["title"])
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] +"\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
