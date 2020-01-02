import unittest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://login.salesforce.com/")
        cls.driver.maximize_window()

    def test_a_login(self):
        self.driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
        self.driver.find_element_by_id("password").send_keys("NewPass@123")
        self.driver.find_element_by_id("Login").click()
        time.sleep(35)

    def test_b_createUser(self):
        self.driver.find_element_by_xpath("//a[@title='Create Menu']").click()
        self.driver.find_element_by_xpath("//span[@class='slds-align-middle']").click()
        time.sleep(8)
        frame1 = self.driver.find_element_by_xpath("//iframe[@title='New User ~ Salesforce - Developer Edition']")
        self.driver.switch_to.frame(frame1)
        self.driver.find_element_by_id("name_firstName").send_keys("surendra firstname")

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
