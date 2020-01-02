import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.bing.com/account/general?ru=")

dd=driver.find_element_by_id("rpp")

#dd means its a dropdown information itself

s=Select(dd)

# s.select_by_index(2)

# s.select_by_value("50")

# s.select_by_visible_text("Auto")

p1=s.options

#options : which will capture all the values in the dropdown and it will store in a varibale when we use print stmt
#it is printing all the weblement but my requirement i want to prein text from all the objects

for element in p1:
    p2=element.get_attribute("value")
    print(p2)




# print(p1)
...
"if we want to select 1st value in the dd then we need to give index as 0" \
"if we want toz elect 2nd value from the dd then we  as 1"
...



time.sleep(5)
driver.quit()