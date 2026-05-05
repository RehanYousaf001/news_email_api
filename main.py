# This is a sample Python script.
from idlelib import query

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from send_email import send_email
query_type="tesla"
url = ("https://newsapi.org/v2/everything?"
       f"q={query_type}&"
       "sortBy=publishedAt&"
       "apiKey=c6dbd3341e0b4d52aadb1359e8a30014&"
       "language=en")

request = requests.get(url)
content = request.json()
print(content)
body = "Subject: Email Implementation in python \n\n"
for article in content["articles"][0:20]:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

