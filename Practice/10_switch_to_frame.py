import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") #switched to embaded frame using frame ID
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("My name is Suraj")

driver.switch_to.default_content() #switched backed to default html
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.quit()
