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

driver.maximize_window()  # maximizes driver window

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ind")

time.sleep(2)

# findind list of country names from the autosuggest dropdown and storing in a variable
country_list = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")

# Printing the number of items in the autosuggest dropdown
print(len(country_list))

# Iterating through the dropdown items
for country in country_list:
    # Clicking on the item with text "India" and breaking out of the loop
    if country.text == "India":
        country.click()
        break
# checking and getting the value of inputted text via get attribute, here the input value is set on backend which we are getting via .get_attribute method
assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value") == "fndia"
