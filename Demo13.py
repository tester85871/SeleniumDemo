import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#below cmd will maxize the browser
driver.maximize_window()
driver.get("https://www.bing.com")

p1=driver.find_elements_by_tag_name("a")

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
        p1[element].send_keys(Keys.TAB)

time.sleep(5)
driver.quit()