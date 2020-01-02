#from selenium import webdriver
import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get('file:///C:/Users/Srujan/Downloads/jar%20files/jar%20files/unexpectedalertcode.html')
driver.implicitly_wait(30)
driver.maximize_window()
time.sleep(20)

a=driver.switch_to.alert

print(a.text)









time.sleep(5)
driver.quit()