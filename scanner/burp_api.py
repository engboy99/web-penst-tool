import requests

BURP_API = "http://127.0.0.1:1337/v1/proxy/history"

def get_requests():
    response = requests.get(BURP_API)
    requests_data = response.json()
    
    captured_requests = []
    
    for request in requests_data:
        url = request['request']['url']
        headers = request['request']['headers']
        captured_requests.append({"url": url, "headers": headers})
        print(f"[+] Captured URL: {url}")
    
    return captured_requests
