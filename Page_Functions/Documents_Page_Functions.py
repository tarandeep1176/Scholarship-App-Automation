from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Documents_Page import DocumentsPageObjects
import time
import os

class DocumentsPageFunctions(DocumentsPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)
            
        def upload_passport(self):
            file_path = os.path.abspath("static/dummy-pdf.pdf")
            file_input = self.wait.until(EC.presence_of_element_located(self.passport_upload_input))
            file_input.send_keys(file_path)
            time.sleep(3)

        def upload_curriculum_vitae(self):
            file_path = os.path.abspath("static/dummy-pdf.pdf")
            file_input = self.wait.until(EC.presence_of_element_located(self.curriculum_vitae_upload_input))
            file_input.send_keys(file_path)
            time.sleep(3)

        def upload_letter_of_motive(self):
            file_path = os.path.abspath("static/dummy-pdf.pdf")
            file_input = self.wait.until(EC.presence_of_element_located(self.letter_of_motive_upload_input))
            file_input.send_keys(file_path)
            time.sleep(3)
            
        def upload_other_document(self):
            file_path = os.path.abspath("static/dummy-pdf.pdf")
            file_input = self.wait.until(EC.presence_of_element_located(self.other_upload_input))
            file_input.send_keys(file_path)
            time.sleep(3)

        def upload_degree(self):
            file_path = os.path.abspath("static/dummy-pdf.pdf")
            file_input = self.wait.until(EC.presence_of_element_located(self.degree_upload_input))
            file_input.send_keys(file_path)
            time.sleep(3)
        
        def click_continue_button(self):
            continueButton = self.wait.until(EC.element_to_be_clickable(self.continue_btn))
            continueButton.click()
            time.sleep(2)