import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set the path to your ChromeDriver executable
chrome_driver_path = 'path/to/chromedriver.exe'

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Create a ChromeDriver instance
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("Suraj Kumar Behera")
driver.find_element(By.NAME, "email").send_keys("suraj.b@naapbooks.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("ProEx")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
print(driver.find_element(By.CLASS_NAME,"alert-success").text)

time.sleep(2)
# driver.close()
