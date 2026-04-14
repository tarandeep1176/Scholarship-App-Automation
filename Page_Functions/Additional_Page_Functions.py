from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Additional_Page import AdditionalPageObjects
import time

class AdditionalPageFunctions(AdditionalPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)
                
        def select_additional_option(self):
            additionalOption = self.wait.until(EC.presence_of_element_located(self.facebook_option))
            additionalOption.click()
            time.sleep(3)
            
        def click_continue_button(self):
            continueButton = self.wait.until(EC.presence_of_element_located(self.continue_btn))
            continueButton.click()
            time.sleep(2)