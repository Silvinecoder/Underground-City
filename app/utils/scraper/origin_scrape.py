import json
from datetime import datetime
from bs4 import BeautifulSoup
from app.db.db_connection import create_session
from app.model.product import Product
from create_request import proxy_request

# Initialize your session object
session = create_session()

def supermarkets_aldi_scrape(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    search_results = soup.find('div', {'id': 'searchResults'})
    data_context = search_results.get('data-context')

    data_dict = json.loads(data_context)
    search_results_list = data_dict.get('SearchResults', [])

    products_data = []

    for result in search_results_list:
        product_name = result.get('FullDisplayName', '')
        product_image_url = result.get('ImageUrl', '')

        new_product = Product(name=product_name, image=product_image_url, supermarket='aldi', country='uk')
        session.add(new_product)

        product_data = {
            'name': product_name,
            'image_url': product_image_url,
            'supermarket': 'aldi',
            'country': 'uk'
        }
        products_data.append(product_data)

    session.commit()

def supermarkets_tesco_scrape(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    product_image = soup.find_all('img', class_='img loaded')
    product_image_urls = [link.get('src') for link in product_image]

  
def scrape():
    # Define your proxy information
    proxy_url = 'http://SvLweHI5oL3yKMUW:C7mz1XuqF48OviAt_country-gb@geo.iproyal.com:12321'
    # Define the URL to scrape
    base_url = 'https://www.lidl.com/search/products/gluten%20free'

    supermarkets_tesco_scrape(proxy_request(base_url, proxy_url, timeout=10))

    # page = 1
    # max_pages = 6

    # while page <= max_pages:
    #     url = base_url.format(page)
    #     html_content = proxy_request(url, proxy_url, timeout=10)

    #     if html_content:
    #         supermarkets_aldi_scrape(html_content)
    #         page += 1
    #     else:
    #         break

    print('Scraping complete!')

scrape()

# Aldi - 'https://groceries.aldi.co.uk/en-GB/Search?keywords=gluten+free&page={}'
