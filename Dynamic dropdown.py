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

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ind")
time.sleep(2)
countrylist=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
print(len(countrylist))
for findcountry in countrylist:
    if findcountry.text=="India":
        findcountry.click()
        break
print(driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value"))
assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value")=="India"

