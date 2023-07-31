import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("Suraj Kumar Behera")
driver.find_element(By.NAME, "email").send_keys("suraj.b@naapbooks.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("ProEx")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
#Static dropdown
staticdrop=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
staticdrop.select_by_index("0")
staticdrop.select_by_visible_text("Female")

driver.find_element(By.XPATH,"//input[@value='Submit']").click()
msg=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success" in msg

time.sleep(2)
# driver.minimize_window()
# driver.close()
