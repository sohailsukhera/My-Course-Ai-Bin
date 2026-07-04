from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.daraz.pk/catalog/?q=Smart%20Phones"

driver = webdriver.Chrome()
driver.get(url)

try:
    # Wait for the item grid wrapper to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-qa-locator='product-item']"))
    )
    
    products = driver.find_elements(By.XPATH, "//div[@data-qa-locator='product-item']")
    
    for product in products:
        try:
            # Update specific selectors based on Daraz layout
            title = product.find_element(By.XPATH, ".//div[@class='title--wFj93']/a").text
            price = product.find_element(By.XPATH, ".//span[@class='currency--GVKjl']").text
            print(f"Product: {title} | Price: {price}")
        except Exception as e:
            continue
finally:
    driver.quit()
    