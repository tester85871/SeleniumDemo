import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://developer.salesforce.com/signup?d=70130000000td6N")

# p1=driver.find_elements_by_tag_name("option")
#
# driver.findElement: it will try to identify in the entire webpage
#     but as per our scrnetio we need to get data from the role dropdown
# so insteat of using driver.fundELmenet ui can use roldd.findElemn

obj=driver.find_element_by_id("job_role")

p1=obj.find_elements_by_tag_name("option")

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

time.sleep(5)
driver.quit()