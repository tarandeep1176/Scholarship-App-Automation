from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Submitted_Page import SubmittedPageObjects
import time


class SubmittedPageFunctions(SubmittedPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15) 

        def check_submitted_text(self):
            try:
                submittedText = self.wait.until(EC.visibility_of_element_located(self.submitted_text))
                actual_message = submittedText.text
                print("Submitted text Extracted as: " + actual_message)
            except:
                print("Form is not submitted.")