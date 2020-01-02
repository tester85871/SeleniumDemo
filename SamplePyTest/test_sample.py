import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

def test_tearDown():
    time.sleep(5)
    driver.quit()

def test_homepage():
    driver.get("https://login.salesforce.com/")
    driver.maximize_window()

    driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
    driver.find_element_by_id("password").send_keys("NewPass@123")
    driver.find_element_by_id("Login").click()


# def test_login():
#     driver.get("https://login.salesforce.com/")
#     driver.maximize_window()
#
#     driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
#     driver.find_element_by_id("password").send_keys("NewPass@123")
#     driver.find_element_by_id("Login").click()
