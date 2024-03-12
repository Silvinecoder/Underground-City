import time 
from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def setup_and_navigate(url, headless=True, implicit_wait=10):
    options = webdriver.ChromeOptions()
    
    if headless:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(implicit_wait)

    driver.get(url)

    return driver

def framework_scraper():
    base_url = 'https://groceries.morrisons.com/search?display=700&entry=gluten%20free'
    driver = setup_and_navigate(base_url)

    product_elements = driver.find_elements(By.CLASS_NAME, 'fop-item')
    print(product_elements)
    print(driver.page_source)

    for product_element in product_elements:
        product_text = product_element.find_element(By.CSS_SELECTOR, 'h4.fop-title').text
        print(product_text)

    driver.quit()
framework_scraper()


# body_element = driver.find_element(By.TAG_NAME, 'body')
# visible_text_content = body_element.text

# # Print the visible text content
# print("Visible Text Content on the Screen:")
# print(visible_text_content)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# load_more_button = driver.find_element(By.CSS_SELECTOR, '[data-test="viewMoreButtonProducts"]')
# if load_more_button.is_displayed():
#     load_more_button.click()
#     # Find the updated list of products after clicking "Load More"
#     updated_product_names = driver.find_elements(By.CSS_SELECTOR, '.detail-card-description')
#     print("Updated Product Names:")
#     print(updated_product_names)
#     print("Updated Page Source:")
#     print(driver.page_source)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


