# Importing the 'time' module for adding delays
import time

# Importing necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Creating Chrome options
chrome_options = Options()

# Adding experimental option to detach the browser window
chrome_options.add_experimental_option("detach", True)

# Creating a service object for the Chrome browser/used to start and stop driver
service_obj = Service()

# Creating a Chrome webdriver instance with the specified service and options
# Here we have created object from webdriver class to access methods present in the class
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()  # maximizes driver window

# Called the get method from webdriver class using the driver object
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()  # Used the title text presnt on link as a value
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys(
    "demo@gmail.com")  # Used the tag names and its index value
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys(
    "Hello@1234")  # Used the tag names and its index value
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys(
    "Hello@1234")  # Used relative css value,syntax=#id attribute
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()  # Used text present on the button

driver.close()
