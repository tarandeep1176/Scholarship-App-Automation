from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Academic_Page import AcademicPageObjects
from selenium.webdriver.common.keys import Keys
import time
import random

class AcademicPageFunctions(AcademicPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)
                
        def select_educational_level(self):
            educationalLevelDropdown = self.wait.until(EC.presence_of_element_located(self.educational_level_dropdown))
            educationalLevelDropdown.click()
            time.sleep(2)
            options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
            random_option = random.choice(options)
            random_option.click()
            time.sleep(2)
            
        def enter_university(self,university):
            universityInput = self.wait.until(EC.presence_of_element_located(self.university_input))
            universityInput.click()
            time.sleep(2)
            universityInput.send_keys(Keys.CONTROL + "a")
            universityInput.send_keys(Keys.DELETE)
            time.sleep(3)
            universityInput.send_keys(university)

        def enter_degree(self,degree):
            degreeInput = self.wait.until(EC.presence_of_element_located(self.degree_input))
            degreeInput.click()
            time.sleep(2)
            degreeInput.send_keys(Keys.CONTROL + "a")
            degreeInput.send_keys(Keys.DELETE)
            time.sleep(3)
            degreeInput.send_keys(degree)

        def select_study_experience(self):
            studyExperienceInput = self.wait.until(EC.presence_of_element_located(self.online_study_mode))
            studyExperienceInput.click()
            time.sleep(3)
            # training_checkbox = self.wait.until(EC.element_to_be_clickable(self.training_checkbox))
            # training_checkbox.click()
            # time.sleep(2)
        
        def enter_other_expertise(self,expertise):
            otherExpertiseInput = self.wait.until(EC.presence_of_element_located(self.other_expertise))
            otherExpertiseInput.click()
            time.sleep(2)
            otherExpertiseInput.send_keys(Keys.CONTROL + "a")
            otherExpertiseInput.send_keys(Keys.DELETE)
            time.sleep(3)
            otherExpertiseInput.send_keys(expertise)

        def click_continue_button(self):
            continueButton = self.wait.until(EC.presence_of_element_located(self.continue_btn))
            continueButton.click()
            time.sleep(2)