...
"we have already insalled selenium package to ur machine" \
"webdriver is a component of selenium which we already know tha" \
"within the editor i want to write my webdriver program for which i need to use those commands " \
"in order to use those commands we need to specify to our editor that use this webdriver from the selenium package whatever" \
"we have installed for hat reason we are using from" \
"" \
"with the line 13 we are specifying that in this class we can create a program for webdriver " \
"as we have successfully imported it" \
"for chrome browser chromedriver.exe" \
"for firefox browser we need geckodriver.exe"
...

#from selenium import webdriver

from selenium import webdriver
# browser=webdriver.Firefox("C:/Users/Srujan/Downloads/geckodriver-v0.26.0-win64/geckodriver.exe")
browser=webdriver.Firefox(executable_path="C:/Users/Srujan/Downloads/geckodriver-v0.26.0-win64/geckodriver.exe")

browser.get('http://seleniumhq.org/')
