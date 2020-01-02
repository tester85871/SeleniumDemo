import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.bing.com/account/general?ru=")

driver.find_element_by_id("rpp").send_keys("10")

time.sleep(5)
driver.quit()