import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.bing.com")

p1=driver.find_elements_by_tag_name("a")
#  we are using FindELements the output willbe collection of
# mutliple objectrs so we can sue a for loop to print all the values
#
# this will rotate the for loop on all the values present in p1
#     initial it will start from 0 index from element onwards
# len(list): total no of valuesin the list
# isSelected
# is displayed also : which will check whether the obejct id siplsyed in the browser or not

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

time.sleep(5)
driver.quit()