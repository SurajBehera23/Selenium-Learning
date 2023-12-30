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

name="Suraj"

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.XPATH, "//input[@onclick='displayConfirm()']").click()
time.sleep(3)
alert = driver.switch_to.alert
alertext = alert.text
print(alertext)
alert.accept()
assert name in alertext


time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Kumar")
driver.find_element(By.XPATH, "//input[@onclick='displayConfirm()']").click()
alert = driver.switch_to.alert
alertext = alert.text
print(alertext)

time.sleep(3)
alert.dismiss()
