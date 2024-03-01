import requests
import threading


def proxy_request(url):
    try:
        # Construct the proxy URL
        proxy_url = f"http://SvLweHI5oL3yKMUW:C7mz1XuqF48OviAt_country-gb@geo.iproyal.com:12321"

        response = requests.get(url, proxies={'http': proxy_url, 'https': proxy_url}, timeout=10)
        print(f"Proxy: {proxy_url}, Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"Valid Proxy: {proxy_url}")
    except Exception as e:
        print(f"Error: {e}")

# Start checking proxies in multiple threads
for t in range(10):
    threading.Thread(target=proxy_request).start()


   