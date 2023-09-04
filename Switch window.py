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
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

openWindows = driver.window_handles # Get a list of handles for all currently open browser windows
driver.switch_to.window(openWindows[1])# Switch the WebDriver's focus to the tab represented by the handle at index 1
savetext=driver.find_element(By.TAG_NAME,"h3").text
print(savetext)
driver.close()
driver.switch_to.window(openWindows[0])#Revert back to parent window
print(driver.find_element(By.TAG_NAME,"h3").text)