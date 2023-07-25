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

driver.maximize_window()
driver.get("https://saakh.naapbooks.com/login")
inputNumber=driver.find_element(By.XPATH,"//input[@class='ant-input ant-input-lg css-yp8pcc']")
inputNumber.send_keys("8093479088")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@class='sc-ewnqHT lkZuBY']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='otp1']").send_keys("123456")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@class='sc-ewnqHT lkZuBY']").click()
time.sleep(1)
