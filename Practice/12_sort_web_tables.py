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
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click() # click on title
clicked_title_values=driver.find_elements(By.XPATH,"//td[1]")

all_clicked_values=[] #got all the values from the loop

for web_values in clicked_title_values:
    all_clicked_values.append(web_values.text) #appending all values got, in to a list
print(all_clicked_values)

original_sorted_list=all_clicked_values.copy() #saving all sorted values to a variable before applying list sort

all_clicked_values.sort()

assert original_sorted_list==all_clicked_values # asserting values before and after applying sort method

driver.quit()