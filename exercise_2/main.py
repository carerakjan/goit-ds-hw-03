'''
    1. make scrapping of site
    2. safe quotes to quotes.json from all pages
    3. safe authors to authors.json
    4. create cloud DB in Atlas
    5. create collections authors and qoutes
    6. import data from jsons to MongoDB
'''

import requests
from bs4 import BeautifulSoup


max_pages = 1
site_url = 'https://quotes.toscrape.com'
quotes_endpoint = 'page'
authors_endpoint = 'author'

def get_page_content(page_endpoint, page_num):
    url = '/'.join([site_url, page_endpoint, str(page_num)])
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')

for i in range(max_pages):
    soup = get_page_content(quotes_endpoint, i+1)
    print(soup)