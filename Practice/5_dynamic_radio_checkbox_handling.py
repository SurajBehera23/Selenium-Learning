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
#clicking on the no2 checkbox

# Find all checkboxes using XPath
get_checkbox_name = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Iterate through each checkbox
for value in get_checkbox_name:
    # Check if the checkbox's name attribute is "checkBoxOption2"
    if value.get_attribute("name") == "checkBoxOption2":
        # Click the checkbox
        value.click()
        # Assert that the checkbox is selected
        assert value.is_selected()
        # Break the loop after finding and interacting with the desired checkbox
        break

# Introduce a delay for 2 seconds
time.sleep(2)

# Find all radio buttons using XPath
get_radio_name = driver.find_elements(By.XPATH, "//input[@class='radioButton']")

# Iterate through each radio button
for radio_value in get_radio_name:
    # Check if the radio button's value attribute is "radio2"
    if radio_value.get_attribute("value") == "radio2":
        # Click the radio button
        radio_value.click()
        # Assert that the radio button is selected
        assert radio_value.is_selected()
        # Break the loop after finding and interacting with the desired radio button
        break

