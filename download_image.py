import requests

# This code is to download an image from the web using just the image url
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Mental_capacities.svg/250px-Mental_capacities.svg.png"

headers = {
    "User-Agent": "MyBot/1.0 (https://anyrandomexample.com/bot; anyrandombutnot@botexample.com)"
}

response = requests.get(url,headers=headers)
print(response)
info = response.content

with open("image.png","wb") as file:
    file.write(info)

