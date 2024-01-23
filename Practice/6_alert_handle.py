# Importing the 'time' module for adding delays
import time
# Importing necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Creating Chrome options
chrome_options = Options()
# Adding experimental option to detach the browser window
chrome_options.add_experimental_option("detach", True)
# Creating a service object for the Chrome browser/used to start and stop driver
service_obj = Service()
# Creating a Chrome webdriver instance with the specified service and options
# Here we have created object from webdriver class to access methods present in the class
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
enter_text=driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Suraj") #enter name in
click_alert= driver.find_element(By.CSS_SELECTOR,"#alertbtn").click() #click on Alert button
alert = driver.switch_to.alert #switch to alert popup
alertext = alert.text #get alert popup text
print(alertext)
alert.accept() #click on OK
assert "Suraj" in alertext

time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Kumar")
driver.find_element(By.XPATH, "//input[@onclick='displayConfirm()']").click() #click on Confirm button
alert = driver.switch_to.alert
alertext = alert.text
print(alertext)

time.sleep(3)
alert.dismiss() #click Cancel button
driver.quit()