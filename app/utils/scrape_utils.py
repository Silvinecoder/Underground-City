import requests
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model.product import Product
from bs4 import BeautifulSoup


engine = create_engine('postgresql://user:celiac@localhost/celiac')
session = Session(bind=engine)

def scrape_and_store_sainsbury_gluten_free_products():
    """Scrape and store gluten free products."""

    url = 'https://www.sainsburys.co.uk/gol-ui/groceries/dietary-and-world-foods/free-from/gluten-free/all-gluten-free/c:1019188'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('li', class_='pt-grid-item')

        for product in products:
            product_name = product.find('h2', class_='pt__info__description').text
            product_image_link = product.find('img', class_='pt-image__link')['href']

            new_product = Product(
                name=product_name,
                image=product_image_link
            )

            session.add(new_product)
    else:
        print('Error: Could not scrape products from the website.')      