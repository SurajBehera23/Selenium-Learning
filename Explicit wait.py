import time

from selenium import webdriver
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

productList=["Onion - 1 Kg","Musk Melon - 1 Kg","Water Melon - 1 Kg","Almonds - 1/4 Kg"]
printlist=[]

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("on")
time.sleep(2)


add_cart = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(add_cart))
for clickadd in add_cart:
    printlist.append(clickadd.find_element(By.XPATH, "h4").text)
    clickadd.find_element(By.XPATH, "div/button").click()

#comparedata
assert printlist==productList


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum total amount
allsum = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for mysum in allsum:
    sum = sum + int(mysum.text)
totalsum=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalsum



driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

#Compare discount is less than total sum
mydiscount=int(driver.find_element(By.CLASS_NAME,"discountAmt").text)
assert mydiscount<totalsum

driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()

time.sleep(3)
driver.close()
