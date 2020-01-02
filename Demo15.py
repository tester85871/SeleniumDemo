import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#below cmd will maxize the browser
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")

fr=driver.find_element_by_class_name("demo-frame")

driver.switch_to.frame(fr)
# driver.switch_to.frame(0)

driver.find_element_by_id("datepicker").send_keys("12/31/2019")

time.sleep(5)
driver.quit()