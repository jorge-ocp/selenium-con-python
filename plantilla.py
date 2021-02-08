import unittest
from pyunitreport import HTMLTestRunner
#para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HomePageTests(unittest.TestCase):
    
    #usamos el decorador classmethod para hacer todo en una sola ventana de chrome
    def setUpClass(sef):
        pass
      
 
    #esta funcion cerrara la ventana de chrome una ves terminada la prueba
 
    def tearDown(self):
        pass
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
    
        