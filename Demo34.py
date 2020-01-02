import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.maximize_window()

driver.execute_script("window.location='https://www.bing.com'")
driver.execute_script("document.getElementById('sb_form_q').value='surendra jaganadam'")
driver.execute_script("document.getElementById('sb_form_go').click();")

time.sleep(5)
driver.quit()