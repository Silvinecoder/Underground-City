import requests


def proxy_request(url, proxy_url, timeout):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, proxies={'http': proxy_url, 'https': proxy_url}, headers=headers, timeout=timeout)
        print(f"Proxy: {proxy_url}, Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"Valid Proxy: {proxy_url}", response.text)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None