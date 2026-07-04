from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"

driver = webdriver.Chrome()
driver.get(url)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "s-item"))
    )
    
    products = driver.find_elements(By.CLASS_NAME, "s-item")
    
    for product in products:
        try:
            title = product.find_element(By.CLASS_NAME, "s-item__title").text
            price = product.find_element(By.CLASS_NAME, "s-item__price").text
            if "Shop on eBay" in title: # Ignore default filler cards
                continue
            print(f"Product: {title} | Price: {price}")
        except:
            continue
finally:
    driver.quit()