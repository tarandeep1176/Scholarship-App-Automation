from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Reference_Page import ReferencePageObjects
from selenium.webdriver.common.keys import Keys
import time
class ReferencePageFunctions(ReferencePageObjects):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def clear_and_type(self, locator, value):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(value)
        time.sleep(1)

    def fill_all_references(self):
        for i in range(3):

            print(f"Filling Reference {i+1}")

            if i != 0:
                self.wait.until(EC.element_to_be_clickable(self.ref_dropdown[i])).click()
                time.sleep(2)

            self.clear_and_type(self.ref_first_name[i], f"First{i+1}")
            self.clear_and_type(self.ref_last_name[i], f"Last{i+1}")
            self.clear_and_type(self.ref_position[i], f"Position{i+1}")
            self.clear_and_type(self.ref_email[i], f"test{i+1}@mail.com")
            self.clear_and_type(self.ref_phone_number[i], f"99999999{i}")
            self.clear_and_type(self.ref_landline_number[i], f"88888888{i}")

    def click_continue_button(self):
        continueButton = self.wait.until(EC.element_to_be_clickable(self.continue_btn))
        continueButton.click()
        time.sleep(2)