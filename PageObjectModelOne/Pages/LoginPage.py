class LoginPageProp():

        def __int__(self,driver):


                self.driver=driver
                self.username_text_field_id = "username"
                self.password_text_field_id = "password"
                self.login_button_id = "Login"

        def enterUsername(self,usernameValue):
                self.driver.find_element_by_id(self.username_text_field_id).send_keys("chaitusarma99@gmail.com")