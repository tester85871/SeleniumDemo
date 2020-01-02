from selenium import webdriver

# driver=webdriver.Chrome("C:/Users/Srujan/Downloads/chromedriver_win32 (9)/chromedriver.exe")
# driver=webdriver.Chrome(executable_path="C:/Users/Srujan/Downloads/chromedriver_win32 (9)/chromedriver.exe")
#whenever we are creating an instance to chrome automtically it is launching a brwser
driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

#get is command which is used to open application on the browser
#driver. for everything??? we are creating an instance to chrome (means the browser itself) and we r stroing tat refernce  in driver
# so moving further if u would lie to perform operations on browser we can use this driver instance itself
driver.get("http://www.bing.com")