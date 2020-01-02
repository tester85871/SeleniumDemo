import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.emirates.com/in/english/")
driver.maximize_window()
#desires tedxt which i capured from the browser n stored in a vairbale
text2="Travel information"
driver.find_element_by_xpath("//a[@data-link='MANAGE']").click()

obj=driver.find_element_by_xpath("//a[@data-link='MANAGE:Before you fly']")

ActionChains(driver).move_to_element(obj).perform()
# movetoElement is a commdn which will move curose to a specific object

val=driver.find_elements_by_xpath("//div[@class='mobile-heading-content-holder' and @role='heading']/span")



for element in range(len(val)):

    text1=val[element].text
    if text1 == text2:
        print(text1)
        val[element].click()
        break

print("test completed")


time.sleep(5)
driver.quit()