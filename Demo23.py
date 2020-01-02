import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.emirates.com/in/english/")
driver.maximize_window()

driver.find_element_by_xpath("//a[@data-link='MANAGE']").click()

obj=driver.find_element_by_xpath("//a[@data-link='MANAGE:Before you fly']")

ActionChains(driver).move_to_element(obj).perform()
# movetoElement is a commdn which will move curose to a specific object

time.sleep(5)
driver.quit()