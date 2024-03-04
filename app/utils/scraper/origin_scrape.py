import json

from datetime import datetime

from bs4 import BeautifulSoup

from app.db.db_connection import create_session
from app.model.product import Product
from create_request import proxy_request


def supermarkets_scrape(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    product_link = soup.find_all(attrs={'data-qa': 'search-product-title'})
    product_names = [name.get('title') for name in product_link]

    product_images = soup.find_all('img', class_='product-image')
    product_image_urls = [link.get('src') for link in product_images]

    products_data = []

    # Loop through the product names and image URLs to add each product to the database
    for name, image_url in zip(product_names, product_image_urls):
        new_product = Product(name=name, image=image_url, supermarket='aldi', country='uk')
        session.add(new_product)

        product_data = {
            'name': name,
            'image_url': image_url,
            'supermarket': 'aldi',
            'country': 'uk'
        }

        products_data.append(product_data)

    session.commit()

    # Append a timestamp to the JSON file name to avoid overwriting
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    json_file_name = f'scraped_aldi_data_{timestamp}.json'
    
    with open(json_file_name, 'w') as json_file:
        json.dump(products_data, json_file, indent=2)

    return product_names, product_image_urls

# Initialize your session object
session = create_session()

    
def scrape():
    # Define your proxy information
    proxy_url = 'http://SvLweHI5oL3yKMUW:C7mz1XuqF48OviAt_country-gb@geo.iproyal.com:12321'

    # Define the URL to scrape
    url = 'https://groceries.aldi.co.uk/en-GB/Search?keywords=gluten+free'

    # Make a proxy request and then scrape the content
    html_content = proxy_request(url, proxy_url)
    if html_content:
        scraper_results = supermarkets_scrape(html_content)
        print(scraper_results)

    supermarkets_scrape(proxy_request(url))

scrape()