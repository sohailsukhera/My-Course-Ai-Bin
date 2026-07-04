import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# eBay standard item structure inside listings
products = soup.find_all('li', {'class': 's-item'})

for product in products:
    title_element = product.find('h3', {'class': 's-item__title'})
    price_element = product.find('span', {'class': 's-item__price'})
    
    if title_element and price_element:
        title = title_element.text.strip()
        price = price_element.text.strip()
        print(f"Product: {title} | Price: {price}")