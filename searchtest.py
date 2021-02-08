import unittest
from pyunitreport import HTMLTestRunner
#para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HomePageTests(unittest.TestCase):
    
    #usamos el decorador classmethod para hacer todo en una sola ventana de chrome
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window() # maximiza la ventana ya que puede haber elementos responsivos que cambien su ubicacion u orden
        driver.implicitly_wait(10) # haremos que espere 15 segundos para empezar a ejecutar la prueba
    
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
        
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
    
    def teste_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")
        
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")
        
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banner = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banner))
    
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')
    
    def test_shopping_car(self):
        shopping_car_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        
        
        
      
 
    #esta funcion cerrara la ventana de chrome una ves terminada la prueba
 
    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
    
        