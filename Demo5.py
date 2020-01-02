import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.bing.com/account/general?ru=")

driver.find_element_by_id("enAS").click()
...
"click is a commnd will toogle the status of the checkbox" \
"but my require nt is i dont want to tooggle it.. based on the status of checked i need o uodat it" \
"" \
"if my checkbox is in checked mode: then simply print a messagew that is already checked" \
"if it is not checked mode then check it and print a message that successfully"
...


time.sleep(5)
driver.quit()