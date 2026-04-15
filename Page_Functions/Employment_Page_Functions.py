from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Employment_Page import EmploymentPageObjects
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import random

class EmploymentPageFunctions(EmploymentPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)
                
        def is_element_present(self, locator, timeout=3):
            try:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
                return True
            except TimeoutException:
                return False
            
        def enter_institution_name(self,institution_name):
            institutionNameInput = self.wait.until(EC.presence_of_element_located(self.institution_name_input))
            institutionNameInput.click()
            time.sleep(2)
            institutionNameInput.send_keys(Keys.CONTROL + "a")
            institutionNameInput.send_keys(Keys.DELETE)
            time.sleep(3)
            institutionNameInput.send_keys(institution_name)

        def enter_position(self,position):
            positionInput = self.wait.until(EC.presence_of_element_located(self.position_input))
            positionInput.click()
            time.sleep(2)
            positionInput.send_keys(Keys.CONTROL + "a")
            positionInput.send_keys(Keys.DELETE)
            time.sleep(3)
            positionInput.send_keys(position)

        def enter_area(self,area):
            areaInput = self.wait.until(EC.presence_of_element_located(self.area_input))
            areaInput.click()
            time.sleep(2)
            areaInput.send_keys(Keys.CONTROL + "a")
            areaInput.send_keys(Keys.DELETE)
            time.sleep(3)
            areaInput.send_keys(area)
            
        def select_worker_category(self):
            workerCategoryDropdown = self.wait.until(EC.presence_of_element_located(self.working_category_dropdown))
            workerCategoryDropdown.click()
            time.sleep(3)
            options = self.wait.until(EC.presence_of_all_elements_located(self.working_category_options))
            random_option = random.choice(options)
            random_option.click()
            
        def enter_activity(self,activity):
            activityInput = self.wait.until(EC.presence_of_element_located(self.activity_input))
            activityInput.click()
            time.sleep(2)
            activityInput.send_keys(Keys.CONTROL + "a")
            activityInput.send_keys(Keys.DELETE)
            time.sleep(3)
            activityInput.send_keys(activity)
        
        def select_seniority_in_position(self):
            seniorityDropdown = self.wait.until(EC.presence_of_element_located(self.senior_in_position_dropdown))
            seniorityDropdown.click()
            time.sleep(2)
            options = self.wait.until(EC.presence_of_all_elements_located(self.working_category_options))
            random_option = random.choice(options)
            random_option.click()
            time.sleep(2)
            
        def enter_monthly_salary(self,monthly_salary):
            monthlySalaryInput = self.wait.until(EC.presence_of_element_located(self.monthly_salary_input))
            monthlySalaryInput.click()
            time.sleep(2)
            monthlySalaryInput.send_keys(Keys.CONTROL + "a")
            monthlySalaryInput.send_keys(Keys.DELETE)
            time.sleep(3)
            monthlySalaryInput.send_keys(monthly_salary)
         
        def select_country(self):
            country = self.wait.until(EC.visibility_of_element_located(self.country_dropdown))
            time.sleep(3)
            country.click()
            time.sleep(3)
            options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
            random_option = random.choice(options)
            random_option.click()
            time.sleep(4)
            
        def select_state(self):
            if self.is_element_present(self.state_dropdown, timeout=3):
                state = self.wait.until(EC.visibility_of_element_located(self.state_dropdown))
                time.sleep(3)
                state.click()
                time.sleep(3)
                options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
                random_option = random.choice(options)
                random_option.click()
                time.sleep(3)
            
        def select_city(self):
            if self.is_element_present(self.city_dropdown, timeout=3):
                city = self.wait.until(EC.visibility_of_element_located(self.city_dropdown))
                time.sleep(3)
                city.click()
                time.sleep(3)
                options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
                random_option = random.choice(options)
                random_option.click()
                time.sleep(3)
            
        def enter_zipcode(self,zipcode):
            zipCodeInput = self.wait.until(EC.visibility_of_element_located(self.zip_code_input))
            zipCodeInput.click()
            time.sleep(3)
            zipCodeInput.send_keys(zipcode)
            time.sleep(3)
        
        def enter_address(self,address):
            addressInput = self.wait.until(EC.visibility_of_element_located(self.address_input))
            addressInput.click()
            time.sleep(3)
            addressInput.send_keys(Keys.CONTROL + "a")
            addressInput.send_keys(Keys.DELETE)
            time.sleep(3)
            addressInput.send_keys(address)
            time.sleep(3)
            
        def enter_landline_number(self,landline_number):
            landlineNumberInput = self.wait.until(EC.presence_of_element_located(self.landline_number_input))
            landlineNumberInput.click()
            time.sleep(3)
            landlineNumberInput.send_keys(Keys.CONTROL + "a")
            landlineNumberInput.send_keys(Keys.DELETE)
            time.sleep(2)
            landlineNumberInput.send_keys(landline_number)
            
        def enter_phone_number(self,phone_number):
            phoneNumberInput = self.wait.until(EC.presence_of_element_located(self.phone_number_input))
            phoneNumberInput.click()
            time.sleep(3)
            phoneNumberInput.send_keys(Keys.CONTROL + "a")
            phoneNumberInput.send_keys(Keys.DELETE)
            time.sleep(2)
            phoneNumberInput.send_keys(phone_number)
            
        def enter_website(self,website):
            websiteInput = self.wait.until(EC.presence_of_element_located(self.website_input))
            websiteInput.click()
            time.sleep(3)
            websiteInput.send_keys(Keys.CONTROL + "a")
            websiteInput.send_keys(Keys.DELETE)
            time.sleep(2)
            websiteInput.send_keys(website)
            
        def click_continue_button(self):
            continueButton = self.wait.until(EC.presence_of_element_located(self.continue_btn))
            continueButton.click()
            time.sleep(2)