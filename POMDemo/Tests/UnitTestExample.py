import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def test_open_chercher_tech(self):
        driver = webdriver.Chrome(executable_path=r"drivers/chromedriver.exe")
        self.driver.get("https://chercher.tech")
        print("Opening CherCherTech")


