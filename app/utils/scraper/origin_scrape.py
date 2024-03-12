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


def scrape():
    proxy_url = 'http://SvLweHI5oL3yKMUW:C7mz1XuqF48OviAt_country-gb@geo.iproyal.com:12321'
    base_url = 'https://groceries.morrisons.com/search?display=700&entry=gluten%20free'

    supermarkets_aldi_scrape(proxy_request(base_url, proxy_url, timeout=4000))

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
# Morrisons - 'https://groceries.morrisons.com/search?entry=gluten%20free'
