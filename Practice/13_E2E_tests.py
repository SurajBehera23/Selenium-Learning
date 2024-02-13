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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[text()='Shop']").click()  # click on Shop
all_prod_title=driver.find_elements(By.XPATH,"//div[@class='card h-100']")

# Iterate through each element
for get_prod_title in all_prod_title:
    # Find the product names within each element
    prod_names = get_prod_title.find_element(By.XPATH, "div/h4/a").text

    # Check if the product name is "Blackberry"
    if prod_names == "Blackberry":
        # If it is, find and click the button within the element
        get_prod_title.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click() # click on checkout button
driver.find_element(By.XPATH,"//button[normalize-space()='Checkout']")
time.sleep(3)
driver.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India"))).click()

driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()