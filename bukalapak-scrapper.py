import requests
from bs4 import BeautifulSoup

url = 'https://www.bukalapak.com/products?'
params = {
    'from' : 'omnisearch',
    'from_keyword_history': 'false',
    'search[keywords]' : 'Tablet',
    'search_source:' : 'omnisearch_keyword',
    'source' : 'navbar'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/113.0.0.0 Safari/537.36'}

html_doc = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(html_doc.text, 'html.parser')
