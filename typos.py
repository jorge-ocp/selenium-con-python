import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window() 
        driver.find_element_by_link_text('Typos').click()
        
    def test_find_typo(self):
        driver = self.driver
        
        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)
        
        tries = 0
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."
        
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh()
        
        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True
 
        
            
            
        self.assertEqual(found, True)
        
        print(f"It took {tries} tries")
            
        
        
        
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()
    
    
        

if __name__ == "__main__":
       unittest.main(verbosity=2)
    