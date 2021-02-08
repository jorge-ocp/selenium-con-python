import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Jorge\Desktop\platzi\selenium con python\chromedriver.exe')
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window() 
        driver.find_element_by_link_text('Add/Remove Elements').click()
    
    def test_add_remove(self):
        elements_added = int(input('How many elements will you add: '))
        elements_removed = int (input('How many elements will you remove: '))
        total_elements = elements_added - elements_removed
        
        
        
        add_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3)
        
        for i in range(elements_added):
            add_button.click()
        
        sleep(3)
            
        for i in range(elements_removed):
            try:
                delete_button = self.driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_button.click()
            except:
                print('You are trying to delete more element than you have')
                break
        
        if total_elements > 0:
            print(f"There are {str(total_elements)} elements on screen")
        else:
            print("There are 0 elements on screen")
                
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()
    
    
        

if __name__ == "__main__":
       unittest.main(verbosity=2)