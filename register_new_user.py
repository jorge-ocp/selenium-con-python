import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window() 
        driver.implicitly_wait(30) 
    
    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #validamos que el botton de create account este habilidado y visible con assertion
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        
        #validamos que crate new customer account es igual al titulo de la ventana
        self.assertEqual('Create New Customer Account', driver.title)
        
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')
        
        
        #revisar que esten habilitados con un assertion
        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())
        
        #envio de datos
        first_name.send_keys('jhon')
        middle_name.send_keys('jose')
        last_name.send_keys('lopez')
        email_address.send_keys('jhonjoselopez@gmail.com')
        password.send_keys('test')
        confirm_password.send_keys('test')
        submit_button.click()
            
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()
        
        

if __name__ == "__main__":
       unittest.main(verbosity=2)
     