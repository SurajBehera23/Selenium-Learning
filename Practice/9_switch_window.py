from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

open_windows_list = driver.window_handles  # lists all open windows
driver.switch_to.window(open_windows_list[1])  # switching between open windows using window index value

get_text_newTab = driver.find_element(By.TAG_NAME, "h3").text
print(get_text_newTab)
driver.close()

driver.switch_to.window(open_windows_list[0])  # after closing child window switched back to parent window

driver.quit()
