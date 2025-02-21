import argparse
from scanner.utils import scan_all

parser = argparse.ArgumentParser(description="Automated Web Pentesting Tool")
parser.add_argument("-u", "--url", required=True, help="Target URL")
args = parser.parse_args()

scan_all(args.url)
