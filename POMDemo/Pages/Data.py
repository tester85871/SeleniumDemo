import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")



