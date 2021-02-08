import unittest
from selenium import webdriver
from time import sleep

class CompareProducts(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("https://google.com")
        driver.maximize_window() 
        driver.implicitly_wait(30) 
        
    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()
        
        driver.back()
        sleep(1)
        driver.forward()
        sleep(1)
        driver.refresh()
        sleep(1)
       
        
        
        
        
            
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()
        
        

if __name__ == "__main__":
       unittest.main(verbosity=2)