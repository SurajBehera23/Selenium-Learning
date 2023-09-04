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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
WindowSwitch = driver.window_handles
driver.switch_to.window(WindowSwitch[1])
savemailID=str(driver.find_element(By.XPATH,"//p[@class='im-para red']").text)
save2=savemailID.split("at")[1].split("with")[0].split(" ")[1].split(" ")[0]
print(save2)

driver.switch_to.window(WindowSwitch[0])
driver.find_element(By.ID,"username").send_keys(save2)
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("abcdef")
driver.find_element(By.XPATH,"(//label/span[@class='checkmark'])[2]").click()
driver.find_element(By.ID,"okayBtn").click()
selectdropdown=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
selectdropdown.select_by_index("1")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
gettext=driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text
print(gettext)
assert gettext=="Empty username/password."

