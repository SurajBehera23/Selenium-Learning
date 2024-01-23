# Importing the 'time' module for adding delays
import time

# Importing necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Creating Chrome options
chrome_options = Options()

# Adding experimental option to detach the browser window
chrome_options.add_experimental_option("detach", True)

# Creating a service object for the Chrome browser/used to start and stop driver
service_obj = Service()

# Creating a Chrome webdriver instance with the specified service and options
# Here we have created object from webdriver class to access methods present in the class
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()#maximizes driver window

# Called the get method from webdriver class using the driver object
driver.get("https://www.google.com") #.get is a method here


# Get the title of the current webpage and store it in the variable
get_the_title = driver.title #.title is a property here

# Print the title to the console
print(get_the_title)

driver.refresh() #refreshes the page

driver.minimize_window() #minimizes driver window

driver.maximize_window()

# Adding a delay of 2 seconds using the 'time' module
time.sleep(2)

# Closing the browser window
driver.close()
