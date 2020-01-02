import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("class will execute only 1 before all the test")
        #  will write logic to launch the browser n open the application weven i wil add maxize browser also
        cls.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        cls.driver.get("https://login.salesforce.com/")
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        print("it will exeucte after all the tests")


    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")


