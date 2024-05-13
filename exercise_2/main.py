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
from author import AuthorParser, Author
from quote import QuoteParser, Quote
from mongo_client import client


def get_page_content(siteurl, endpoint):
    url = "/".join([siteurl, endpoint])
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


def create_db():
    db = client.hbs_exercise_2
    return db.quotes, db.authors


def main():
    max_pages = 5
    site_url = "https://quotes.toscrape.com"
    quotes_json = "quotes.json"
    authors_json = "authors.json"
    quotes = Serializer(factory=lambda _: Quote(**_)).load(quotes_json)
    authors = Serializer(factory=lambda _: Author(**_)).load(authors_json)

    if not quotes or not authors:
        for i in range(max_pages):
            soup = get_page_content(site_url, f'page/{i + 1}')
            for tag in soup.select(selector=".quote"):
                quote = QuoteParser(tag).data
                quotes.append(quote)
        
        authors_urls = {q.author_url for q in quotes}
        
        for endpoint in sorted(authors_urls):
            soup = get_page_content(site_url, endpoint[1:])
            author = AuthorParser(soup).data
            authors.append(author)
        
        quotes.save(quotes_json)
        authors.save(authors_json)
    
    quotes_db, authors_db = create_db()
    quotes_db.delete_many({})
    authors_db.delete_many({})
    quotes_db.insert_many(quotes.to_json())
    authors_db.insert_many(authors.to_json())

if __name__ == '__main__':
    main()
