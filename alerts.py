import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window() 
        driver.implicitly_wait(30) 
        
    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_id('search')
        search_field.clear() #como buena practica aplicamos limpieza a la barra de busqueda
        
        search_field.send_keys('tee')
        search_field.submit()
        
        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()
        
        alert = driver.switch_to_alert()
        alert_text = alert.text
        
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        
        alert.accept()
        
        
        
        
            
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()
        
        

if __name__ == "__main__":
       unittest.main(verbosity=2)