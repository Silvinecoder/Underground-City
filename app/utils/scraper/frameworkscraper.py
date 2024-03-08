import time 
from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Define the Chrome webdriver options
options = webdriver.ChromeOptions()
# Set the Chrome webdriver to run in headless mode for scalability
options.add_argument("--headless")

driver = Chrome(options=options)
driver.implicitly_wait(10)

base_url = 'https://www.lidl.com/search/products/gluten%20free'

driver.get(base_url)
time.sleep(20)

# Find list of products
product_names = driver.find_elements(By.CSS_SELECTOR, '.detail-card-description')
print(product_names)

try:
  view_more_button_span = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, "//button//span[contains(@class, 'clickable-label') and text()='view more']"))
  )
  view_more_button_span.click()
except TimeoutException:
  print("Timed out waiting for 'view more' button to be clickable.")
finally:
  print(driver.page_source)
