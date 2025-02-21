from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (optional)
    options.add_argument("--disable-gpu")  # Fixes some Linux issues
    options.add_argument("--no-sandbox")  # Required for some environments
    options.add_argument("--disable-dev-shm-usage")  # Fixes shared memory issues

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def scan_xss(url):
    """Function to scan for XSS vulnerabilities."""
    driver = get_driver()
    driver.get(url)
    print(f"Scanning {url} for XSS vulnerabilities...")
    # Add your XSS scanning logic here
    driver.quit()
    print("Scan completed.")

# Example usage (for debugging, remove this in production)
if __name__ == "__main__":
    scan_xss("http://example.com")
