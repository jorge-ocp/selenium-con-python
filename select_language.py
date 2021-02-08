import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select  #no servira para seleccionar elementos del dropdown

class LanguageOptions(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window() 
        driver.implicitly_wait(30) 
        
    
    def test_select_langugage(self):
        #guardamos el orden de como aparece en la pagina, para despues comparar
        exposed_options = ['English', 'French', 'German' ]
        
        #creamos una lista para almacenar las opciones
        active_options = []
        
        #creamos una variable para acceder a las opciones del dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))
        
        #creamos un assert para comprobar que la cantidad de opciones es correcta
        #options permite ingresar directamente a las opciones del dropdown
        self.assertEqual(3, len(select_language.options))
        
        #creamos un for para agregarle el texto de la pagina en la variable active_options
        for option in select_language.options:
            active_options.append(option.text)
        
        #usamos assert para verificar que la lista de opciones disponibles y activas sean identicas
        self.assertListEqual(exposed_options, active_options)
        
        self.assertEqual('English', select_language.first_selected_option.text)
        
        #seleccionamos "German" por el texto visible
        select_language.select_by_visible_text('German')
        
        #verificamos que el sitio cambio a Aleman
        #preguntamos a selenium si la url del sitio contiene esas palabras
        self.assertTrue('store=german' in self.driver.current_url)
        
        #volvemos a seleccionar ingles con index 0
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)
        
    
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()
        
        

if __name__ == "__main__":
       unittest.main(verbosity=2)