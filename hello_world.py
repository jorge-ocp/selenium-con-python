import unittest
from pyunitreport import HTMLTestRunner
#para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    #usamos el decorador classmethod para hacer todo en una sola ventana de chrome
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        
    #esta funcion visitara la pagina para aplicar la prueba
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
    
    #esta funcion cerrara la ventana de chrome una ves terminada la prueba
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))
    
        
    
    
    