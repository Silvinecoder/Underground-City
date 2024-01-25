from model.product import Product
from bs4 import BeautifulSoup

def scrape_and_store_gluten_free_products():
    """Scrape and store gluten free products."""
    response = requests.get(url)


    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', class_='product')

        for product in products:
            product_name = product.find('h3', class_='product__title').text
            product_description = product.find('p', class_='product__description').text
            product_label = product.find('p', class_='product__label').text
            product_ingredients = product.find('p', class_='product__ingredients').text
            nutrition_data = product.find('p', class_='product__nutrition-data').text
            product_location = product.find('p', class_='product__location').text

            new_product = Product(
                product_name=product_name,
                product_description=product_description,
                product_label=product_label,
                product_ingredients=product_ingredients,
                nutrition_data=nutrition_data,
                product_location=product_location
            )

            session.add(new_product)
            session.commit()
      else:
        print('Error: Could not scrape products from the website.')      