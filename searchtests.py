import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SearchTest(unittest.TestCase):
    
    #usamos el decorador classmethod para hacer todo en una sola ventana de chrome
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window() # maximiza la ventana ya que puede haber elementos responsivos que cambien su ubicacion u orden
        driver.implicitly_wait(30) # haremos que espere 15 segundos para empezar a ejecutar la prueba
     
    
           
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        
        search_field.send_keys('tee')
        search_field.submit()
        
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        
        search_field.send_keys('salt shaker')
        search_field.submit()
        
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))
    
        
      
   
 
    #esta funcion cerrara la ventana de chrome una ves terminada la prueba
 
    def tearDown(self):
        self.driver.quit()
        
        

if __name__ == "__main__":
       unittest.main(verbosity=2)
    
        