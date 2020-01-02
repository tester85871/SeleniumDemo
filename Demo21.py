import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#below cmd will maxize the browser
driver.maximize_window()
driver.get("https://jqueryui.com/tooltip/")


fr=driver.find_element_by_class_name("demo-frame")

driver.switch_to.frame(fr)


obj=driver.find_element_by_id("age")

p1=obj.get_attribute("title")
print("tooltip message is : " +p1)

time.sleep(8)
driver.quit()