# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2026-03-28&sortBy=publishedAt&apiKey=c6dbd3341e0b4d52aadb1359e8a30014"

request = requests.get(url)
content = request.text
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["url"])