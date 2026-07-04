import requests
from bs4 import BeautifulSoup

url = "https://www.alibaba.com/trade/search?SearchText=Auto+Accessories"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Look for search item divs
products = soup.find_all('div', {'class': 'fy23-search-card'})

if not products:
    print("BeautifulSoup was blocked by Alibaba structural walls or CAPTCHA.")

for product in products:
    title = product.find('h2')
    price = product.find('span', {'class': 'search-card-e-price-main'})
    
    if title:
        print(f"Product: {title.text.strip()} | Price: {price.text.strip() if price else 'N/A'}")