from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Reference_Page import ReferencePageObjects
import time


class ReferencePageFunctions(ReferencePageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def fill_all_references(self):
            for i in range(3):

                print(f"Filling Reference {i+1}")

                if i != 0:
                    self.wait.until(EC.element_to_be_clickable(self.ref_dropdown[i])).click()
                    time.sleep(2)
                self.wait.until(EC.visibility_of_element_located(self.ref_first_name[i])).send_keys(f"First{i+1}")
                time.sleep(2)
                self.driver.find_element(*self.ref_last_name[i]).send_keys(f"Last{i+1}")
                time.sleep(2)
                self.driver.find_element(*self.ref_position[i]).send_keys(f"Position{i+1}")
                time.sleep(2)
                self.driver.find_element(*self.ref_email[i]).send_keys(f"test{i+1}@mail.com")
                time.sleep(2)
                self.driver.find_element(*self.ref_phone_number[i]).send_keys(f"99999999{i}")
                time.sleep(2)
                self.driver.find_element(*self.ref_landline_number[i]).send_keys(f"88888888{i}")
                time.sleep(2)
                
        def click_continue_button(self):
            continueButton = self.wait.until(EC.presence_of_element_located(self.continue_btn))
            continueButton.click()
            time.sleep(2)
