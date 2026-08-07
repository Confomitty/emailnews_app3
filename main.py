import requests

api_key = "66f46eff71c54001a25699a975669917"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "sortBy=publishedAt&apiKey=66f46eff71c54001a25699"
       "a975669917")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])