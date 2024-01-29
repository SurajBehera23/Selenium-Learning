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
# Adding experimental option to detach the browser window
chrome_options.add_experimental_option("detach", True)
# Creating a service object for the Chrome browser/used to start and stop driver
service_obj = Service()
# Creating a Chrome webdriver instance with the specified service and options
# Here we have created object from webdriver class to access methods present in the class
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# search product
search_input = driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']")
search_input.send_keys("Be")

time.sleep(2)
# add searched products to cart by add to cart button
add_to_cart = driver.find_elements(By.XPATH, "//button[contains(text(),'ADD TO CART')]")

print(len(add_to_cart))
for cart_click in add_to_cart:
    if cart_click.text == "ADD TO CART":
        cart_click.click()

# click on cart image
click_on_cart = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']")
click_on_cart.click()

# click on checkout button
click_checkout = driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
click_checkout.click()

# explicit wait until locator is present on page
wait = WebDriverWait(driver, 3)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

# enter discount code on box
enter_discount = driver.find_element(By.TAG_NAME, "input")
enter_discount.send_keys("rahulshettyacademy")

# clcick on apply button
click_apply = driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']")
click_apply.click()

# explicit wait until locator is present on page
wait = WebDriverWait(driver, 3)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

# get successful apply message and assert it
get_promo_success = driver.find_element(By.CSS_SELECTOR, "span[class='promoInfo']").text
assert "Code applied ..!" in get_promo_success

#sum validation
get_total_amount = driver.find_elements(By.XPATH, "//td[5]/p")
total_table_amount =0
for get_amount in get_total_amount:
    total_table_amount=total_table_amount+int(get_amount.text)
print(total_table_amount)

on_screen_total=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert on_screen_total==total_table_amount
