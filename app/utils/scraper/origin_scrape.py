import json
import requests

from bs4 import BeautifulSoup

from app.db.db_connection import create_session
from app.model.product import Product


def proxy_request(url, proxy_url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, proxies={'http': proxy_url, 'https': proxy_url}, headers=headers, timeout=10)
        print(f"Proxy: {proxy_url}, Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"Valid Proxy: {proxy_url}")
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None

def supermarkets_scrape(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    product_link = soup.find_all('a', class_='text-default-font')
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

    with open('scraped_sainsbury_data.json', 'w') as json_file:
        json.dump(products_data, json_file, indent=2)

    return product_names, product_image_urls

# Initialize your session object
session = create_session()

# Define your proxy information
proxy_url = 'http://SvLweHI5oL3yKMUW:C7mz1XuqF48OviAt_country-gb@geo.iproyal.com:12321'

# Define the URL to scrape
url = 'https://groceries.aldi.co.uk/en-GB/Search?keywords=gluten+free'

# Make a proxy request and then scrape the content
html_content = proxy_request(url, proxy_url)
if html_content:
    scraper_results = supermarkets_scrape(html_content)
    print(scraper_results)