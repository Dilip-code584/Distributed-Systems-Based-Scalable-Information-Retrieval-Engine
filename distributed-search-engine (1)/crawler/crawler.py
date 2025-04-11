# Distributed web crawler using multiprocessing and sockets
import requests, os
from bs4 import BeautifulSoup
from multiprocessing import Pool

def fetch_url(url):
    try:
        response = requests.get(url, timeout=3)
        return url, response.text
    except:
        return url, None

def save_page(url, html, output_dir="data/raw_html"):
    if html:
        filename = os.path.join(output_dir, url.replace("/", "_") + ".html")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

def crawl(urls):
    with Pool(4) as p:
        results = p.map(fetch_url, urls)
    for url, html in results:
        save_page(url, html)
