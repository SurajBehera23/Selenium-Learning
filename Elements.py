import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()

a = "https://saakh.naapbooks.com/login"
driver.get(a)
print(driver.current_url)
print(driver.title)
driver.find_element(By.XPATH, "//input[@name='mobileNO']").send_keys("8093479088")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='sc-ewnqHT lkZuBY']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='otp1']").send_keys("123456")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='sc-ewnqHT lkZuBY']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//i[@class='fas fa-users']").click()
time.sleep(2)
driver.back()
driver.refresh()
driver.minimize_window()
driver.close()
