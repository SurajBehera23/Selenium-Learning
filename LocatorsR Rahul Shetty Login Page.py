import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/auth/login")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("demo@gmail.com")
