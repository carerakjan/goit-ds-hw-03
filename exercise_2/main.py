"""
    1. make scrapping of site
    2. safe quotes to quotes.json from all pages
    3. safe authors to authors.json
    4. create cloud DB in Atlas
    5. create collections authors and qoutes
    6. import data from jsons to MongoDB
"""

import requests
from bs4 import BeautifulSoup
from serializer import Serializer
from author import AuthorParser
from quote import QuoteParser


max_pages = 5
site_url = "https://quotes.toscrape.com"


def get_page_content(endpoint):
    url = "/".join([site_url, endpoint])
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


quotes = []
for i in range(max_pages):
    soup = get_page_content(f'page/{i + 1}')
    for tag in soup.select(selector=".quote"):
        quote = QuoteParser(tag).data
        quotes.append(quote)

serializer = Serializer(quotes)
serializer.save("quotes.json")


authors_urls = {q.author_url for q in quotes}


authors = []
for endpoint in authors_urls:
    soup = get_page_content(endpoint[1:])
    author = AuthorParser(soup).data
    authors.append(author)

serializer = Serializer(authors)
serializer.save("authors.json")
