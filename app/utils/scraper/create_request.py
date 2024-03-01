import requests
import csv
import random


# Use proxies to scrape data from the web without the chance of being blocked.
proxy_list = []

# We have a proxy list that we can use to make requests to the web.

with open('/home/corsaire/Documents/Personal projects/celiac-python/app/tests/proxies.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        proxy_list.append(row[0])

def get_next_proxy():
    return proxy_list.pop(0) 

def create_request(url):
    try:
        proxy = get_next_proxy()
        # If you want to rotate proxies, you can uncomment the line below
        # proxy_list.append(proxy)  # Add the used proxy back to the end of the list

        # Create a header to represent a user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, headers=headers, timeout=10)

        if response.status_code == 200:
            print(response.status_code)
            return response.content
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        # Handle errors (e.g., retry with a different proxy)
        return None

   