from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.amazon.com/gp/browse.html?node=6563140011"

driver = webdriver.Chrome()
driver.get(url)

try:
    # Wait until product grid/cards are loaded
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result'] | //span[@class='a-size-base-plus']"))
    )
    
    # Scroll slightly to trigger lazy loading
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)

    # Grabbing items
    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    
    for product in products:
        try:
            title = product.find_element(By.XPATH, ".//h2//span").text
            price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
            print(f"Product: {title} | Price: ${price}")
        except:
            continue
finally:
    driver.quit()