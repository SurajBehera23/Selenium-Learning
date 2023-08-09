import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Create an ActionChains object to perform complex interactions with the WebDriver
action = ActionChains(driver)

# Move the cursor to the element with the specified ID "mousehover"
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# Move the cursor to the element with the specified LINK_TEXT "Reload" and then click it
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
