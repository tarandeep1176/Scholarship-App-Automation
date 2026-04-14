from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Summary_Page import SummaryPageObjects
import time

class SummaryPageFunctions(SummaryPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)
                
        def click_terms_and_conditions_checkbox(self):
            checkbox = self.wait.until(EC.presence_of_element_located(self.terms_and_conditions_checkbox))
            checkbox.click()
            time.sleep(3)
            
        def click_submit_button(self):
            submitButton = self.wait.until(EC.presence_of_element_located(self.submit_btn))
            submitButton.click()
            time.sleep(2)