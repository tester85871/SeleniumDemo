import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#below cmd will maxize the browser
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")
time.sleep(8)

fr=driver.find_element_by_class_name("demo-frame")

driver.switch_to.frame(fr)
obj=driver.find_element_by_id("draggable")

# ActionChains.drag_and_drop_by_offset(obj,50,50).perform()

ActionChains(driver).drag_and_drop_by_offset(obj,150,150).perform()

#until and inless we import the packge we cant see all the supported methods
# so lets import thr proper package and then see the various methods in that
# perform(): which is used to performt hat ipeationon the browser




time.sleep(8)
driver.quit()