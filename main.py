# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2026-03-28&sortBy=publishedAt&apiKey=c6dbd3341e0b4d52aadb1359e8a30014"

request = requests.get(url)
content = request.text

body = ""
for article in content["articles"]:
    if article['title'] is not None:
        body += article['title'] + "\n" + article['description'] + 2*"\n"
        body = body.encode("utf-8")

send_email(body)

