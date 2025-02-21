import threading
from .sql_injection import run_sqlmap
from .xss_scanner import scan_xss
from .idor_scanner import scan_idor
from .ssrf_scanner import scan_ssrf

def scan_all(target_url):
    threads = []
    tests = [run_sqlmap, scan_xss, scan_idor, scan_ssrf]

    for test in tests:
        thread = threading.Thread(target=test, args=(target_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("[+] Scanning Completed!")
