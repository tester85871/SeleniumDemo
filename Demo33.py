import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("file:///C:/Users/Srujan/Downloads/jar%20files/jar%20files/unexpectedalertcode.html")
driver.maximize_window()
time.sleep(15)

a=driver.switch_to.alert

# a.text #which will get the text
# a.send_keys("data") #will enter data into that field
# a.accept() #click on ok button
# a.dismiss() #cancel on the

print(a.text)

a.accept()

print("succesfully handled alerts")




time.sleep(5)
driver.quit()