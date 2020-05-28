import requests
from bs4 import BeautifulSoup
import time
from multiprocessing import Process, Queue, Pool
import threading
import sys

proxies = {  # define the proxies which you want to use
    'http': 'http://195.22.121.13:443',
    'https': 'http://195.22.121.13:443',
}
startTime = time.time()
qcount = 0
products = []
prices = []
ratings = []
no_pages = 9


def scrap(product, page):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.61 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
        "Connection": "close", "Upgrade-Insecure-Requests": "1"
    }

    resp = requests.get(f'https://www.amazon.in/s?k={product}&page={page}', headers=headers)
    content = resp.content
    soup = BeautifulSoup(content, "html.parser")
    for item in soup.find_all('div', attrs={'class': 's-include-content-margin s-border-bottom s-latency-cf-section'}):
        price = item.find('span', attrs={'class', 'a-price-whole'})
        if price is not None:
            print(price.text)
        else:
            print("Currently Unavailable")
        name = item.find('span', attrs={'class', 'a-size-medium a-color-base a-text-normal'})
        print(name.text)
        rating = item.find('span', attrs={'class', 'a-icon-alt'})
        print(rating.text)
        # prices.append(price.text)

    print(len(prices))


scrap('laptops', '1')
