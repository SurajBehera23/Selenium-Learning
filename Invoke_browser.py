import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://www.google.com")
time.sleep(2)
driver.close()

