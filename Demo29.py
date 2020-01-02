import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.w3schools.com/tags/default.asp")
driver.maximize_window()


beforeNumber="//tr["
afterNumberTag="]/td[1]"
afterNumberDesc="]/td[2]"

# beforeNumber+2,3,4(neess to come from for loop) +afternumber

for _ in range(2,5):
    xp1=beforeNumber+str(_)+afterNumberTag
    # xp1=//tr[2]/td[1]
    tagName=driver.find_element_by_xpath(xp1).text
    print(tagName)


    xp2=beforeNumber+str(_)+afterNumberDesc
    desc=driver.find_element_by_xpath(xp2).text
    print(desc)






time.sleep(5)
driver.quit()