import random

from bs4 import BeautifulSoup

from db.db_connection import create_session
from create_request import create_request
from model.product import Product


session = create_session()
 
def supermarkets_scrape(url):
  soup = BeautifulSoup(url, 'html.parser')

  product_link = soup.find_all('a', class_='pt__link')
  product_names = [name.get('title') for name in product_link]

  product_images = soup.find_all('img', attrs={'data-test-id': 'pt-image'})
  product_image_urls = [link.get('src') for link in product_images]

# Loop through the product names and image URLs to add each product to the database
  for name, image_url in zip(product_names, product_image_urls):
    new_product = Product(name=name, image=image_url)
    session.add(new_product)

  session.commit()


  return product_names, product_image_urls

# do proxy try https://www.youtube.com/watch?v=JJ0St6OmTp0&ab_channel=NetworkChuck
# db connection
# file