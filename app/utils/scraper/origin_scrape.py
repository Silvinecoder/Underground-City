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
    # Define your proxy information
    proxy_url = 'http://SvLweHI5oL3yKMUW:C7mz1XuqF48OviAt_country-gb@geo.iproyal.com:12321'
    # Define the URL to scrape
    base_url = 'https://groceries.aldi.co.uk/en-GB/Search?keywords=gluten+free&page={}'
    page = 1
    max_pages = 4

    while page <= max_pages:
        url = base_url.format(page)
        html_content = proxy_request(url, proxy_url, timeout=10)

        if html_content:
            supermarkets_aldi_scrape(html_content)
            page += 1
        else:
            break

    print('Scraping complete!')

scrape()


# def supermarkets_scrape(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')

#     product_link = soup.find_all(attrs={'data-context': 'search-product-title'})
#     product_names = [name.get('title') for name in product_link]

#     product_images = soup.find_all('img', class_='product-image')
#     product_image_urls = [link.get('src') for link in product_images]

#     # Loop through the product names and image URLs to add each product to the database
#     for name, image_url in zip(product_names, product_image_urls):
#         # Uncomment this line if you want to see the individual product name and image URL
#         new_product = Product(name=name, image=image_url, supermarket='aldi', country='uk')
#         session.add(new_product)

#         # Uncomment these lines if you want to collect data for further processing
#         product_data = {
#             'name': name,
#             'image_url': image_url,
#             'supermarket': 'aldi',
#             'country': 'uk'
#         }
#         products_data.append(product_data)

#     # Uncomment this line if you want to commit changes to the database
#     session.commit()

#     # Uncomment these lines if you want to save the data to a JSON file
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     json_file_name = f'scraped_aldi_data_{timestamp}.json'
#     with open(json_file_name, 'w') as json_file:
#         json.dump(products_data, json_file, indent=2)

#     return product_names, product_image_urls

