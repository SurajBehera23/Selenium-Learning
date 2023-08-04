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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("on")
time.sleep(2)

add_cart = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div/div[3]/button")

for res in add_cart:
    res.click()
