import requests
import random

    # Use proxies to scrape data from the web without the chance of being blocked.
proxy_list = [
    'http://',
    'http://',
]    

# From my understanding the random proxy happens as a multiple request to the same website. So we are different people rather than one person
def get_random_proxy():
    return random.choice(proxy_list)

def create_request(url):
    try:
      proxy = get_random_proxy()
      # we create a header to represent a user agent
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
          # Add any additional headers as needed
      }

      response = requests.get(url, proxies={'http': proxy, 'https': proxy}, headers=headers, timeout=10)
      if response.status_code == 200:
            return response.content
      else:
          print(f"Request failed with status code: {response.status_code}")
          return None
    except Exception as e:
        print(f"Error: {e}")
        # Handle errors (e.g., retry with a different proxy)
        return None


   