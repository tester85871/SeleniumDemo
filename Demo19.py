import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#below cmd will maxize the browser
driver.maximize_window()
driver.get("https://www.emirates.com/in/english/?")
time.sleep(3)

driver.find_element_by_xpath("//a[@data-link='MANAGE']").click()

obj=driver.find_element_by_xpath("//a[@data-link='MANAGE:Before you fly']")



ActionChains(driver).move_to_element(obj).perform()



#until and inless we import the packge we cant see all the supported methods
# so lets import thr proper package and then see the various methods in that
# perform(): which is used to performt hat ipeationon the browser




time.sleep(8)
driver.quit()