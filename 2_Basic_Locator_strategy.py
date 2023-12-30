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

# Called the get method from webdriver class using the driver object
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Input email
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")  # Used name attribute

# Input password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")  # Used ID attribute

# Click the checkbox
driver.find_element(By.ID, "exampleCheck1").click()

#Select the static dropdown using select class
dropdown=Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
dropdown.select_by_index(1)

# Input name
driver.find_element(By.XPATH, "//input[@minlength='2']").send_keys(
    "Suraj Kumar Behera")  # Used XPATH selector,syntax= //tagname[@attribute='value']

# Click submit
driver.find_element(By.CSS_SELECTOR,
                    "input[type='submit']").click()  # #Used CSS selector,syntax= tagname[attribute='value']

# Get and print success message
get_success_message_text = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(get_success_message_text)

# Assert success message
assert "The Form has been submitted successfully!." in get_success_message_text

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()  # Used relative css value,syntax=#id attribute
driver.find_element(By.CSS_SELECTOR, ".ng-untouched.ng-pristine.ng-valid").send_keys(
    " Vicky")  # Used relative css value,syntax=.class attribute
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".ng-untouched.ng-pristine.ng-valid").clear()
