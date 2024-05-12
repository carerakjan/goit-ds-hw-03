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
import serializer
from author import AuthorParser
from quote import QuoteParser


max_pages = 5
site_url = "https://quotes.toscrape.com"
quotes_endpoint = "page"


def get_page_content(page_endpoint, page_num):
    url = "/".join([site_url, page_endpoint, str(page_num)])
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


quotes = []
for i in range(max_pages):
    soup = get_page_content(quotes_endpoint, i + 1)
    for tag in soup.select(selector=".quote"):
        quote = QuoteParser(tag).data
        quotes.append(quote)
serializer.save("quotes.json", [q.serialize() for q in quotes])


authors_urls = {q.author_url for q in quotes}


authors = []
for aut_url in authors_urls:
    endpoint, unique_part = aut_url[1:].split("/")
    soup = get_page_content(endpoint, unique_part)
    author = AuthorParser(soup).data
    authors.append(author)
serializer.save("authors.json", [a.serialize() for a in authors])
