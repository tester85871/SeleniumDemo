import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.bing.com")
driver.maximize_window()

driver.find_element_by_id("sb_form_q").send_keys("surem")
time.sleep(5)

p1=driver.find_elements_by_xpath("//li[@class='sa_sg']")

#below line will print total no of values in the list
print(len(p1))


for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

#let me try to capture screenshot
# inorder to capture screenwe need to methion in which location it needs to capture
# we need o specify file location and file name also as an input to this function


driver.get_screenshot_as_file("C:/Users/Srujan/Desktop/Selenium/python/demo22.png")
time.sleep(1)
driver.quit()