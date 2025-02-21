import os

def run_sqlmap(target_url):
    print(f"[+] Scanning for SQL Injection: {target_url}")
    command = f"sqlmap -u {target_url} --batch --dbs"
    os.system(command)
import os
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

# Function to run sqlmap for SQL injection testing
def run_sqlmap(target_url):
    if not validate_url(target_url):
        print(f"[!] Invalid URL: {target_url}")
        return
    
    print(f"[+] Scanning for SQL Injection: {target_url}")
    command = f"sqlmap -u {target_url} --batch --dbs"
    os.system(command)

# Example usage
run_sqlmap("http://example.com")
