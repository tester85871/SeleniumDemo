import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.maximize_window()
#below 3 lines will enter uname, pswc, click on login button
driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
driver.find_element_by_id("password").send_keys("NewPass@123")
driver.find_element_by_id("Login").click()
time.sleep(35)
#there is a reason for giving 35sec here which we will study

#below 2 lines will click on create n then it will create user
driver.find_element_by_xpath("//a[@title='Create Menu']").click()
driver.find_element_by_xpath("//span[@class='slds-align-middle']").click()
#i can use findElemtns capture all the infor uhse a forloop and print all the textws n clcik on desired object as discssed in demo25example
# u can also use demo24 example option which is identify the count 1st and write customixex xpath which is
# (xpath)[count]
time.sleep(8)

# //below 2 lines will switch tothe frame in user creation oage
frame1=driver.find_element_by_xpath("//iframe[@title='New User ~ Salesforce - Developer Edition']")
driver.switch_to.frame(frame1)

# below line will enter firstnane
driver.find_element_by_id("name_firstName").send_keys("surendra firstname")
#whenever we r working with SF app : every peage has a frame before execution let us cross check this html content
# once to see whether the desired object is in framr or nit

driver.find_element_by_xpath("//img[@alt='Call Center Lookup (New Window)']").click()
time.sleep(5)

first=driver.window_handles[0]
second=driver.window_handles[1]
# above 2 cmnds will captur both window information
# now we need to ask our webdriver to switch to 2nd window

driver.switch_to.window(second)
# swith to frame in the new qwindow
frame2=driver.find_element_by_id("searchFrame")
driver.switch_to.frame(frame2)

# below cmd will enter a value in the new window
driver.find_element_by_id("lksrch").send_keys("surendra")
driver.find_element_by_name("go").click()

# driver.switch_to_default_content()

driver.switch_to.window(first)

time.sleep(5)
driver.quit()