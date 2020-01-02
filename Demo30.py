import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.w3schools.com/tags/default.asp")
driver.maximize_window()
driver.implicitly_wait(30)


table=driver.find_element_by_xpath("//table[@class='w3-table-all notranslate']/tbody")

tablerows=table.find_elements_by_tag_name("tr")

# WebDriverWait(driver,10).until(expected_conditions.alert_is_present)

# WebDriverWait(driver,10).until(EX.alert_is_present)

#inorder to lnpw how many rows r there we can use len method

print(len(tablerows))

beforeNumber="//tr["
afterNumberTag="]/td[1]"
afterNumberDesc="]/td[2]"

# beforeNumber+2,3,4(neess to come from for loop) +afternumber

for _ in range(2,len(tablerows)):
    xp1=beforeNumber+str(_)+afterNumberTag
    # xp1=//tr[2]/td[1]
    tagName=driver.find_element_by_xpath(xp1).text
    print(tagName)


    xp2=beforeNumber+str(_)+afterNumberDesc
    desc=driver.find_element_by_xpath(xp2).text
    print(desc)

time.sleep(5)
driver.quit()