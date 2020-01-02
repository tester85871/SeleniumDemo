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

driver.find_element_by_id("datepicker").click()
# i obserevdt hat dates r starting with tagname as a
# so we can use linkText command to perfrom click operations
# uysually if anything is starting with tagnmas a if u want to epform click operation opnthat
# we can use linkText

driver.find_element_by_xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

driver.find_element_by_link_text("31").click()
time.sleep(5)
driver.quit()