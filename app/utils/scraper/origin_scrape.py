import json

from bs4 import BeautifulSoup

from app.db.db_connection import create_session
from app.model.product import Product


session = create_session()
 
def supermarkets_scrape(url, json_filename='scraped_sainsbury_data.json'):
  soup = BeautifulSoup(url, 'html.parser')

  product_link = soup.find_all('a', class_='pt__link')
  product_names = [name.get('title') for name in product_link]

  product_images = soup.find_all('img', attrs={'data-test-id': 'pt-image'})
  product_image_urls = [link.get('src') for link in product_images]

  products_data = []

# Loop through the product names and image URLs to add each product to the database
  for name, image_url in zip(product_names, product_image_urls):
    new_product = Product(name=name, image=image_url, supermarket='sainsburys', country='uk')
    session.add(new_product)

    product_data = {
        'name': name,
        'image_url': image_url,
        'supermarket': 'sainsburys',
        'country': 'uk'
    }

    products_data.append(product_data)

  session.commit()

  with open(json_filename, 'w') as json_file:
        json.dump(products_data, json_file, indent=2)


  return product_names, product_image_urls

# do proxy try https://www.youtube.com/watch?v=JJ0St6OmTp0&ab_channel=NetworkChuck