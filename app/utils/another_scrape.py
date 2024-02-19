from selenium.webdriver.common.by import By
from urllib.error import ContentTooShortError
from urllib3.exceptions import NewConnectionError, ConnectionError, MaxRetryError
import time
import pandas as pd
import os
import datetime
from initiate_driver import create_headless_driver
import re
from selenium.common.exceptions import (TimeoutException, WebDriverException, NoSuchElementException,
                                        StaleElementReferenceException)
import signal
import subprocess

removed_items = []

def scrape_aldi_data():
    # Specify the URL
    url = 'https://groceries.aldi.co.uk/en-GB/Search?keywords=gluten+free'

    # Product Names
    product_name_CSS = '#vueSearchResults .p.text-default-font'

    # Specify the path of the new folder
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    folder_path = f"/Users/cristianasimoes/Documents/side-projects/Underground-City/app/utils/ALDI_DATA/{timestamp}"
    print('hello')

    class TimedOut(Exception):
        print('The custom error TimedOut has been raised')
        pass

    # Define a signal handler function for the timeout
    def signal_handler(signum, frame):
        raise TimedOut("Timeout occurred")

    def force_quit(process):
        subprocess.run(['pkill', process])

    # Register the signal handler for the SIGALRM signal
    signal.signal(signal.SIGALRM, signal_handler)

    # Initialise the browser outside the function
    browser = 'Chrome'
    driver = create_headless_driver(browser=browser)
    print(driver)
    driver.set_script_timeout(30)

    names_text = []
    page_numbers_names = []
    last_page_number = []
    error_list = []

    try:
        driver.get(url)
        last_page_numbers = driver.find_elements(By.CSS_SELECTOR, 'ul .d-flex-inline.pt-2')
        last_page_number.extend([number.text for number in last_page_numbers])
        last_page_number = last_page_number[1]
        last_page_number = re.sub(r'\D', '', last_page_number)  # Remove non-digit characters
        print(f'The last page number is: {last_page_number}')
    except (NoSuchElementException, ConnectionError, NewConnectionError, MaxRetryError,
            StaleElementReferenceException, TimeoutError, ValueError, IndexError):
        # If the initial attempt fails, reload the page and try again
        driver.quit()
        time.sleep(10)
        driver.get(url)
        last_page_numbers = driver.find_elements(By.CSS_SELECTOR, 'ul .d-flex-inline.pt-2')
        last_page_number.extend([number.text for number in last_page_numbers])
        last_page_number = last_page_number[1]
        last_page_number = re.sub(r'\D', '', last_page_number)  # Remove non-digit characters
        print(f'The last page number is: {last_page_number}')

    page = 1
    while page <= int(last_page_number):
        try:
            # Set the timeout for the page request
            signal.alarm(30)  # Set the timeout to 30 seconds

            driver.get(f'{url}&page={page}')
            time.sleep(3)

            names = driver.find_elements(By.CSS_SELECTOR, product_name_CSS)
            names_text.extend([name.text for name in names])
            page_numbers_names.extend([page] * len(names))

            # Reset the alarm after a successful page request
            signal.alarm(0)

            # Iterate up a loop
            page += 1

        except (TimedOut, TimeoutException, WebDriverException, ConnectionError, StaleElementReferenceException,
                NewConnectionError, MaxRetryError, TimeoutError, ContentTooShortError) as exc:
            print(f'Request error for page {page}')
            # force_quit(process='chromedriver')
            driver.quit()
            time.sleep(30)
            error_list.append(exc)
            driver = create_headless_driver(browser=browser)
            continue  # Skip to the next page if there is an error

    names_data = {
        'names': names_text,
        'page_number': page_numbers_names  # Add page numbers list
    }

    df_names = pd.DataFrame(names_data)

    # Create the new folder if it doesn't exist
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)

    # Save the modified dataframes to a new JSON file
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    df_names.to_json(f'{folder_path}/df_names_{timestamp}.json', orient='records')

    force_quit(process='chromedriver')
    driver.quit()
    print('done')


def force_quit(process):
    subprocess.run(['pkill', process])

print('started aldi')    
scrape_aldi_data()
