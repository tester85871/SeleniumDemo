import xlrd
import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("http://www.bing.com")
driver.maximize_window()



loc=("C:/Users/Srujan/Desktop/Selenium/python/DataDriven.xlsx")

wb=xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

p1=sheet.cell(2,0).value
print(p1)

print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.nrows):
    p2 = sheet.cell(i, 0).value
    print(p2)
    driver.find_element_by_id("sb_form_q").clear()
    driver.find_element_by_id("sb_form_q").send_keys(p2)
    time.sleep(1)

time.sleep(5) #which will wait for 2 seconds
driver.quit() # which will termate thr bwower m release