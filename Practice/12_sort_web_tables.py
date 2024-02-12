# Importing the 'time' module for adding delays
import time
# Importing necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Creating Chrome options
chrome_options = Options()
# chrome_options.add_argument("headless") # used to run chrome in headless mode
# Adding experimental option to detach the browser window
chrome_options.add_experimental_option("detach", True)
# Creating a service object for the Chrome browser/used to start and stop driver
service_obj = Service()
# Creating a Chrome webdriver instance with the specified service and options
# Here we have created object from webdriver class to access methods present in the class
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

