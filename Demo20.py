import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#below cmd will maxize the browser
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")


fr=driver.find_element_by_class_name("demo-frame")

driver.switch_to.frame(fr)
obj=driver.find_element_by_id("draggable")



# below cmd will capture the height n width of the object
s=obj.size
# below cmd will capture x n y corrnidate of the object
l=obj.location

print(obj.get_attribute("class"))

print(s)
print(l)



time.sleep(8)
driver.quit()