import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
getvalues = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(getvalues))
for singlevalue in getvalues:
    if singlevalue.get_attribute("value") == "option2":
        singlevalue.click()
        assert singlevalue.is_selected()
        break

getradio = driver.find_elements(By.XPATH, "//input[@type='radio']")

print(len(getradio))
for allradio in getradio:
    if allradio.get_attribute("value") == "radio3":
        allradio.click()
        break
print(driver.find_element(By.ID, "displayed-text").is_displayed())

driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID, "displayed-text").is_displayed()