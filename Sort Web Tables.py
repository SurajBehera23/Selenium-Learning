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

NewVegList=[]

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
getvalue=Select(driver.find_element(By.ID,"page-menu"))
getvalue.select_by_index(1)
driver.find_element(By.XPATH,"//tr/th[1]").click()#clicked on5>10
getveglist=driver.find_elements(By.XPATH,"//tr/td[1]")#got all the webelements prsent on that xpath
for myveglist in getveglist:
    NewVegList.append(myveglist.text)#got the text of webelements and stored them in new list
print(NewVegList)#printed the new list
originalsortedVeg=NewVegList.copy()#stored browser sorted list in new variable to compare with selenium sorted list
NewVegList.sort()#sorted the list using selenium method
assert originalsortedVeg==NewVegList#verified  if orginal web sort = selenium sort
driver.close()