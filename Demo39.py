#from selenium import webdriver
import time

from selenium import webdriver
# browser=webdriver.Firefox("C:/Users/Srujan/Downloads/geckodriver-v0.26.0-win64/geckodriver.exe")
driver=webdriver.Firefox(executable_path="C:/Users/Srujan/Downloads/geckodriver-v0.26.0-win64/geckodriver.exe")

driver.get('http://seleniumhq.org/')
driver.implicitly_wait(30)







time.sleep(5)
driver.quit()