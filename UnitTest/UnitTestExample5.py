# import unittest
# from selenium import webdriver
# import time
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class MyTestCase(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         #  will write logic to launch the browser n open the application weven i wil add maxize browser also
#         # cls.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
#         cls.driver = webdriver.Chrome(ChromeDriverManager().install())
#         cls.driver.get("https://login.salesforce.com/")
#         cls.driver.maximize_window()
#
#     # def test_login(self):
#     #     time.sleep(3)
#
#      def test_login(self):
#          #in this test i want to create logic which will login into the app
# # # means it will enter uname, enter pswd, click on login button abd wait for sometine until we enter verificationc deo manually
#          self.driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
#          self.driver.find_element_by_id("password").send_keys("NewPass@123")
#          self.driver.find_element_by_id("Login").click()
#          time.sleep(35)
#
#
# # def test_createAccount(self):
# #     # i want to write logic to perform click o[eration n] on create user and enter firstanem
# #     self.driver.find_element_by_xpath("//a[@title='Create Menu']").click()
# #     self.driver.find_element_by_xpath("//span[@class='slds-align-middle']").click()
# #     time.sleep(8)
# #     frame1 = self.driver.find_element_by_xpath("//iframe[@title='New User ~ Salesforce - Developer Edition']")
# #     self.driver.switch_to.frame(frame1)
# #     # below line will enter firstnane
# #     self.driver.find_element_by_id("name_firstName").send_keys("surendra firstname")
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#
#
#     @classmethod
#     def tearDownClass(cls):
#         # i will logic to wait for sometime and terminate the browser
#         time.sleep(5)
#         cls.driver.quit()
#
#
#
#
#
