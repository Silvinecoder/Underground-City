import os
import json
import html
from bs4 import BeautifulSoup
from app.db.db_connection import create_session
from app.model.product import Product

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
        
        product_image_url = search_result.find('img', class_='tile-image').get('src', '')
        print(product_image_url)

        category = data_dict.get('category', '')
        print(category)

        if '/' in category:
            category_parts = category.split('/')
            category_href = '/'.join(category_parts[:-1])  # excluding the last part (product)
            category_name = category_parts[-2]
        else:
            category_name = ''

        product_data = {
            'name': product_name,
            'image_url': product_image_url,
            'category': category_name,
            'supermarket': 'auchan',
            'country': 'PT'
        }

        products_data.append(product_data)

    # Add products to the database
    for product_data in products_data:
        new_product = Product(
            name=product_data['name'],
            image=product_data['image_url'],
            category=product_data['category'],
            supermarket=product_data['supermarket'],
            country=product_data['country']
        )
        session.add(new_product)

    session.commit()

    return product_data

def supermarkets_pingo_doce_scrape(json_content, session):
    data = json.loads(json_content)
    products_data = []

    for product in data:
        product_name = product.get('name', '')
        product_name = sanitize_string(product_name)
        product_image_url = product.get('image', 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Pingo_Doce_logo.png')
        category = product.get('category', '')

        product_data = {
            'name': product_name,
            'image_url': product_image_url,
            'category': category,
            'supermarket': 'pingo_doce',
            'country': 'PT'
        }

        products_data.append(product_data)

    # Add products to the database
    for product_data in products_data:
        new_product = Product(
            name=product_data['name'],
            image=product_data['image_url'],
            category=product_data['category'],
            supermarket=product_data['supermarket'],
            country=product_data['country']
        )
        session.add(new_product)

    session.commit()

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

        product_data = {
            'name': product_name,
            'image_url': product_image_url,
            'supermarket': 'continent',
            'country': 'PT',
            'category': category_data['category']  # Access category from the corresponding dictionary
        }

        products_data.append(product_data)

    # Add sorted products to the database
    for product_data in products_data:
        new_product = Product(
            name=product_data['name'],
            image=product_data['image_url'],
            category=product_data['category'],
            supermarket=product_data['supermarket'],
            country=product_data['country']
        )
        session.add(new_product)

    session.commit()

    return product_data

def scrape_and_save():
    html_content = read_html()
    json_content = read_json()
    
    with create_session() as session:
        products_data = supermarkets_pingo_doce_scrape(json_content, session)
        # products_data = supermarkets_auchan_scrape(html_content, session)
        print(f'Total products scraped: {len(products_data)}')

scrape_and_save()
