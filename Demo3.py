import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")

driver.find_element_by_id("sb_form_q").send_keys("surendra jagandam")
driver.find_element_by_xpath("//label[@for='sb_form_go']").click()

# in the last seesion we crated 1 scenario it launched  another browser , we are not writing any commands to close the browser
# usually our systme will allocate some memory : if we are not terminating the browser means we will encounter , and
#speed of our machine will reduce
# it will close the browser and will relase the memory which is aloocated

time.sleep(5) #which will wait for 2 seconds
driver.quit() # which will termate thr bwower m release