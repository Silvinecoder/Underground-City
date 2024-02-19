
# Rest of the code continues after this point...

# import requests
# from bs4 import BeautifulSoup
# from requests.exceptions import RequestException, Timeout
# from app.db.db_connection import create_session
# from app.model.product import Product  # Adjust the import based on your actual model

# def scrape_products(url, session, product_list_class, product_name_class, max_retries=3):
#     page = 1
#     while True:
#         try:
#             # Set a timeout for the request (adjust the value as needed)
#             response = requests.get(f'{url}?&page={page}', timeout=10)
#             response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

#             print(response.status_code)

#             soup = BeautifulSoup(response.content, 'html.parser')

#             # Find parent elements containing product titles
#             product_lists = soup.find_all('ul', class_=product_list_class)
#             print(product_lists)

#             if not product_lists:
#                 break  # No more pages to scrape

#             for product_list in product_lists:
#                 # Within each product list, find product titles (h3 and h4)
#                 product_titles = product_list.find_all(['h3', 'h4'], class_=product_name_class)

#                 if product_titles:
#                     # Extract and print product titles
#                     for title in product_titles:
#                         product_name = title.text.strip()
#                         print(product_name)

#                         # Create a Product object and add it to the session
#                         new_product = Product(name=product_name)
#                         session.add(new_product)

#                         print(f'Added product: {product_name}')

#             # Iterate to the next page
#             page += 1

#         except (Timeout, RequestException) as exc:
#             print(f'Error: {exc}')

#             # Retry logic
#             max_retries -= 1
#             if max_retries <= 0:
#                 print('Max retries reached. Exiting.')
#                 break

#             print(f'Retrying... Remaining retries: {max_retries}')
#         except Exception as exc:
#             print(f'Unexpected error: {exc}')
#             break

# # Use the create_session function to create a database session
# session = create_session()

# categories_list = ['fresh-food']

# for category in categories_list:
#     names_text = []
#     # ... (other variables)

#     url = f'https://groceries.aldi.co.uk/en-GB/{category}'  # Adjust the URL based on your requirements
#     product_list_class = 'product-list'  # Adjust based on the structure of the target webpage
#     product_name_class = 'product-name'  # Adjust based on the structure of the target webpage

#     scrape_products(url, session, product_list_class, product_name_class)

# # Commit the changes to the database
# session.commit()

# # Close the session after the scraping is done
# session.close()

# # def scrape_products(url, session, product_list_class, product_name_class):
# #     try:
# #         # Set a timeout for the request (adjust the value as needed)
# #         response = requests.get(url, timeout=10)
# #         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

# #         print(response.status_code)

# #         soup = BeautifulSoup(response.content, 'html.parser')

# #         # Find parent elements containing product titles
# #         product_lists = soup.find_all('ul', class_=product_list_class)
# #         print(product_lists)

# #         if product_lists:
# #             for product_list in product_lists:
# #                 # Within each product list, find product titles (h3 and h4)
# #                 product_titles = product_list.find_all(['h3', 'h4'], class_=product_name_class)

# #                 if product_titles:
# #                     # Extract and print product titles
# #                     for title in product_titles:
# #                         product_name = title.text.strip()
# #                         print(product_name)

# #                         # Create a Product object and add it to the session
# #                         new_product = Product(name=product_name)
# #                         session.add(new_product)

# #                         print(f'Added product: {product_name}')
# #                 else:
# #                     print('No product titles found in the product list.')
# #         else:
# #             print('No product lists found on the page.')

# #     except Timeout:
# #         print('Error: Request timed out. Please check your internet connection or try again later.')
# #     except RequestException as e:
# #         print(f'Error: An unexpected error occurred - {e}')

# # # Use the create_session function to create a database session
# # session = create_session()

# # # Scrape Morrisons products
# # # morrisons_url = 'https://groceries.morrisons.com/search?entry=bread'
# # # morrisons_product_list_class = 'fops fops-regular fops-shelf'
# # # morrisons_product_name_class = 'fop-title'
# # # scrape_products(morrisons_url, session, morrisons_product_list_class, morrisons_product_name_class)

# # # Scrape Tesco products
# # tesco_url = 'https://www.tesco.com/groceries/en-GB/search?query=juice&icid=tescohp_sws-1_m-ft_in-juice_out-juice'
# # tesco_product_list_class = 'product-list gridf'
# # tesco_product_name_class = 'styles__H3-oa5soe-0 gbIAbl'
# # scrape_products(tesco_url, session, tesco_product_list_class, tesco_product_name_class)

# # # Commit the changes to the database
# # session.commit()

# # # Close the session after the scraping is done
# # session.close()
