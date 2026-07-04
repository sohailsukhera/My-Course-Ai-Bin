import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.daraz.pk/catalog/?q=Smart%20Phones"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Daraz puts product data inside a window.pageData script tag
script_tags = soup.find_all('script')
data_found = False

for script in script_tags:
    if script.string and "window.pageData=" in script.string:
        # Extract JSON using regular expression
        json_text = re.search(r'window\.pageData\s*=\s*({.*?});', script.string)
        if json_text:
            data = json.loads(json_text.group(1))
            # Access product items from JSON array
            items = data.get('mods', {}).get('listItems', [])
            for item in items:
                print(f"Product: {item.get('name')} | Price: RS {item.get('price')}")
            data_found = True
            break

if not data_found:
    print("Could not find dynamic data via BeautifulSoup. Use Selenium.")