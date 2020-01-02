import time
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains

class loginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("data")


    def test_login_valid(self):
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.driver.get("https://login.salesforce.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
        self.driver.find_element_by_id("password").send_keys("NewPass@123")
        self.driver.find_element_by_id("Login").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()



#below 3 lines will enter uname, pswc, click on login button

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
if __name__ =='__main__':
    unittest.main(verbosity=2)