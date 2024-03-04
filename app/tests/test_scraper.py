import os
import json

from datetime import datetime
from bs4 import BeautifulSoup

from app.db.db_connection import create_session
from app.model.product import Product


def read_html():
      relative_path = './aldi.html'
      absolute_path = os.path.abspath(relative_path)
      with open(absolute_path) as file:
        return file.read()

    
def supermarkets__test_scrape(html_content):
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

def scraper_test():
    # expectedNames = []
    # expectedUrls = ['https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\10.11.22\\4088600206486_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\25.05.23\\4088600206462_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\25.05.23\\4088600206479_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/16.05.22 (2)/5060014570130_0.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/5449000031341_c56e9b7073c14d1ab5f6e1ff351f3050.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/5449000004451_034bb5f73dfa4efebcdbd35ae274aabc.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\16.08.23\\5060059531028_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\19.01.24\\5021727000475_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\19.09.23\\5060059530151_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\08.01.24\\5060426810114_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\10.08.23\\4088600518022_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\02.11.22\\4088600334776_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/4002971207309_9f72b7ef0ffb4dd8bbbc2daf1463128e.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/4002971207705_de43a52a1e5e47dbbb8d21bd1f18f64a.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\07.06.23\\4088600135304_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/4088600146683_d592e146a26346a58c4d5a20f0e801ec.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/26.04.23/4088600167824_0.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\16.05.22 (2)\\5060302740030_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\12.05.22\\5449000058386_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\12.08.22 (2)\\5449000601971_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\08.09.23\\5019503018974_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\08.09.23\\5019503019056_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\19.05.22\\5449000131836_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\12.08.22 (2)\\54491472_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\25.05.22\\54491496_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/04.10.22/5010082132792_0.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/04.10.22/5449000669902_0.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/04.10.22/5449000673039_0.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\5000193034559_2ddeb7013f0348f5b6ee8dc3eed82fb9_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\10.10.23\\5010228012926_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/23.10.23/8719200269743_0.jpg', 'https://aldprdproductimages.azureedge.net/media/$Aldi_GB/23.10.23/8719200269934_0.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\04.02.2022\\50107452_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\20.01.23\\50382811_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\23.02.22\\4088600434179_0_M.jpg', 'https://aldprdproductimages.azureedge.net/media/resized\\$Aldi_GB\\10.08.23\\4088600013756_0_M.jpg'] 
    
    scrapedData = supermarkets__test_scrape(read_html())

    # assert scrapedData == (expectedUrls)

    print(scrapedData)


# Initialize your session object outside the scraper function
session = create_session()
scraper_test()
