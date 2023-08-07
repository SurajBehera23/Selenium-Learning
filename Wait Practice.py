import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("on")
time.sleep(2)

add_cart = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(add_cart))

for clickadd in add_cart:
    clickadd.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
# time.sleep(10)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()