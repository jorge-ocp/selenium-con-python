import unittest
from pyunitreport import HTMLTestRunner
#para comunicarnos con el navegador usamos webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):
    
    #usamos el decorador classmethod para hacer todo en una sola ventana de chrome
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window() # maximiza la ventana ya que puede haber elementos responsivos que cambien su ubicacion u orden
        driver.implicitly_wait(10) # haremos que espere 15 segundos para empezar a ejecutar la prueba
    
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
    
    def tearDown(self):
        self.driver.quit()
        

    #funcion que nos ayudara a encotnrar los elementos de acuerdo a sus parametros
    def is_element_present(self, how, what): #how es el tipo de selector y what el valor que tiene
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True
        
        
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
    
        