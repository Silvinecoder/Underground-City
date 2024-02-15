import requests
from sqlalchemy.orm import session
from bs4 import BeautifulSoup

from app.model.product import Product

class Scraper:
    def __init__(self, session):
        self.session = session

    def scrape_and_store_sainsbury_gluten_free_products(self):
        url = 'https://www.sainsburys.co.uk/gol-ui/groceries/dietary-and-world-foods/free-from/gluten-free/all-gluten-free/c:1019188'
        response = requests.get(url)
        print('hello?')

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products = soup.find_all('li', class_='pt-grid-item')
            print('inside the if?')

            for product in products:
                product_name = product.find('h2', class_='pt__info__description').text
                product_image_link = product.find('img', class_='pt-image__link')['href']
                new_product = Product(
                    name=product_name,
                    image=product_image_link
                )
                print('inside the for loop?')
                self.session.add(new_product)

            self.session.commit()
        else:
            print('Error: Could not scrape products from the website.')

scraper = Scraper(session)
scraper.scrape_and_store_sainsbury_gluten_free_products()