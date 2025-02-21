import requests
import time
import re

# Validate URL format using regex
def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' 
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex, url) is not None

# Function to scan for IDOR vulnerability
def scan_idor(target_url, param_name, start_id, end_id):
    if not validate_url(target_url):
        print(f"[!] Invalid URL: {target_url}")
        return
    
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url
    
    for i in range(start_id, end_id + 1):
        url = f"{target_url}?{param_name}={i}"
        try:
            response = requests.get(url, timeout=10)  # 10 seconds timeout
            if response.status_code == 200 and "private" in response.text.lower():
                print(f"[+] Possible IDOR Found: {url}")
        except requests.exceptions.Timeout:
            print(f"[!] Timeout error while accessing {url}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error accessing {url}: {e}")
            time.sleep(2)  # Sleep for 2 seconds before retrying

# Example usage
scan_idor("http://example.com", "user_id", 1, 100)
