import os
import json
import html
from bs4 import BeautifulSoup

from app.db.db_connection import create_session

from app.model.product import Product
from app.model.category import Category
from app.model.attribute import Attribute
from app.model.supermarket import Supermarket
from app.model.supermarket_product_pair import SupermarketProductPair

def read_html():
    relative_path = './auchan.html'
    absolute_path = os.path.abspath(relative_path)
    with open(absolute_path) as file:
        return file.read()
    
def read_json():
    relative_path = './pingo_doce.json'
    absolute_path = os.path.abspath(relative_path)
    with open(absolute_path) as file:
        return file.read()

def sanitize_string(string):
    return html.unescape(string)

def add_products_to_db(products_data, session):
    for product_data in products_data:
        category_name = product_data.get('category', '')
        attribute_type = product_data.get('attribute_type', '')  # Updated key name
        supermarket_name = product_data.get('supermarket_name', '')
        country = product_data.get('country', '')

        category = Category.get_or_create(session, category_name)
        attribute = Attribute.get_or_create(session, attribute_type)
        supermarket = Supermarket.get_or_create(session, supermarket_name, country)
        product = Product.get_or_create(session, product_data['name'], product_data['image_url'], category, attribute)

        session.add(product)

        if supermarket:
            SupermarketProductPair.get_or_create(session, product, supermarket)

    session.commit()

def create_product_data(product_name, product_image_url, category, attribute_type, supermarket_name, country):
    return {
        'name': product_name,
        'image_url': product_image_url,
        'category': category,
        'attribute_type': attribute_type, 
        'supermarket_name': supermarket_name,
        'country': country
    }

def supermarkets_auchan_scrape(html_content, session):
    soup = BeautifulSoup(html_content, 'html.parser')

    search_results = soup.find_all('div', class_='product-tile')
    products_data = []

    for search_result in search_results:
        # Extracting data from the 'data-gtm' attribute
        data_gtm = search_result.attrs.get('data-gtm', '{}')
        data_dict = json.loads(data_gtm)

        product_name = data_dict.get('name', '')
        product_name = sanitize_string(product_name)
        print(product_name)
        
        picture_element = search_result.find('picture')
        link_element = picture_element.find('link')
        product_image_url = link_element.get('href', '').strip()
        print(product_image_url)

        category = data_dict.get('category', '')
        print(category)

        if '/' in category:
            category_parts = category.split('/')
            category_name = category_parts[-2]
        else:
            category_name = ''

        product_data = create_product_data(product_name, product_image_url, category_name, 'gluten-free', 'Auchan', 'PT')

        products_data.append(product_data)

    add_products_to_db(products_data, session)

    return product_data

def supermarkets_pingo_doce_scrape(json_content, session):
    data = json.loads(json_content)
    products_data = []

    for product in data:
        product_name = product.get('name', '')
        product_name = sanitize_string(product_name)
        product_image_url = product.get('image', 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Pingo_Doce_logo.png')
        category = product.get('category', '')

        product_data = create_product_data(product_name, product_image_url, category, 'pingo_doce', 'PT')

        products_data.append(product_data)

    add_products_to_db(products_data, session)

    return product_data

def supermarkets_continent_scrape(html_content, session):
    soup = BeautifulSoup(html_content, 'html.parser')

    search_results = soup.find_all('div', class_='ct-image-container')
    search_category = soup.find_all('div', class_='product-tile')
    products_data = []
    product_category_data = []  # Changed variable name to avoid confusion

    for search_category in search_category:
        data_context = search_category.get('data-product-tile-impression')
        data_dict = json.loads(data_context)
        product_category = data_dict.get('category', '')

        # Append each category dictionary to the product_category_data list
        product_category_data.append({
            'category': product_category,
        })

    for search_result, category_data in zip(search_results, product_category_data):  # Zip both lists together
        data_context = search_result.get('data-confirmation-image')
        data_dict = json.loads(data_context)
        product_name = data_dict.get('alt', '')
        product_name = sanitize_string(product_name)
        product_image_url = data_dict.get('url', '')

        product_data = create_product_data(product_name, product_image_url, category_data['category'], 'continent', 'PT')

        products_data.append(product_data)

    add_products_to_db(products_data, session)

    return product_data

def scrape_and_save():
    html_content = read_html()
    json_content = read_json()
    
    with create_session() as session:
        # products_data = supermarkets_pingo_doce_scrape(json_content, session)
        products_data = supermarkets_auchan_scrape(html_content, session)
        print(f'Total products scraped: {len(products_data)}')

scrape_and_save()
