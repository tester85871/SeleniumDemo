import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.bing.com/account/general?ru=")

p1=driver.find_element_by_id("enAS").is_selected()
print(p1)

#is_selected() true or false : if is checked mode then it will return else it will return fals4

if p1:
    print("already checked")
else:
    driver.find_element_by_id("enAS").click()
    print("successfully checked it")




time.sleep(5)
driver.quit()