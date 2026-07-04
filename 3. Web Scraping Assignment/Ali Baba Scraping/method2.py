from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.alibaba.com/trade/search?SearchText=Auto+Accessories"

# Tip: To pass Alibaba detection, sometimes headless needs to be turned off
driver = webdriver.Chrome()
driver.get(url)

try:
    # Wait for target card container
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'fy23-search-card')]"))
    )
    
    products = driver.find_elements(By.XPATH, "//div[contains(@class, 'fy23-search-card')]")
    
    for product in products:
        try:
            title = product.find_element(By.XPATH, ".//h2").text
            # Prices can vary based on wholesale quantity tiers
            price = product.find_element(By.XPATH, ".//div[contains(@class, 'price')]").text
            print(f"Product: {title} | Price: {price}")
        except:
            continue
finally:
    driver.quit()