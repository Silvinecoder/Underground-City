import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options


def create_headless_driver(browser='Chrome'):
    if browser == 'Chrome':
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        # Disable SSL certificate verification
        options.add_argument('--ignore-certificate-errors')

        driver = uc.Chrome(options=options)
        driver.maximize_window()
        
    elif browser == 'Firefox':
        raise ValueError("Undetected Firefox is not currently supported")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver