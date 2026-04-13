from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Address_Page import AddressPageObjects
from selenium.webdriver.common.keys import Keys
import time
import random

class AddressPageFunctions(AddressPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)
                
        def click_add_email(self):
            addEmailButton = self.wait.until(EC.presence_of_element_located(self.add_email_btn))
            addEmailButton.click()
            time.sleep(2)
            
        def enter_email(self,email):
            emailInput = self.wait.until(EC.presence_of_element_located(self.email_input))
            emailInput.click()
            time.sleep(2)
            emailInput.send_keys(Keys.CONTROL + "a")
            emailInput.send_keys(Keys.DELETE)
            time.sleep(3)
            emailInput.send_keys(email)
            
        def enter_mobile_number(self,mobile_number):
            mobileNumberInput = self.wait.until(EC.presence_of_element_located(self.phone_number_input))
            mobileNumberInput.click()
            time.sleep(2)
            mobileNumberInput.send_keys(Keys.CONTROL + "a")
            mobileNumberInput.send_keys(Keys.DELETE)
            time.sleep(3)
            mobileNumberInput.send_keys(mobile_number)

        def enter_whatsapp_number(self,whatsapp_number):
            whatsappNumberInput = self.wait.until(EC.presence_of_element_located(self.whatsapp_number))
            whatsappNumberInput.click()
            time.sleep(3)
            whatsappNumberInput.send_keys(Keys.CONTROL + "a")
            whatsappNumberInput.send_keys(Keys.DELETE)
            time.sleep(2)
            whatsappNumberInput.send_keys(whatsapp_number)

        def select_type_of_housing(self):
            typeOfHousingDropdown = self.wait.until(EC.presence_of_element_located(self.type_of_housing_dropdown))
            typeOfHousingDropdown.click()
            time.sleep(2)
            options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
            random_option = random.choice(options)
            random_option.click()
            time.sleep(2)
            
        def select_housing_condition(self):
            housingConditionDropdown = self.wait.until(EC.visibility_of_element_located(self.housing_condition_dropdown))
            housingConditionDropdown.click()
            time.sleep(2)
            options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
            random_option = random.choice(options)
            random_option.click()
            time.sleep(2)
            
        def select_country(self):
            country = self.wait.until(EC.visibility_of_element_located(self.country_of_residence_dropdown))
            time.sleep(3)
            country.click()
            time.sleep(3)
            countryInput = self.wait.until(EC.visibility_of_element_located(self.country_input))
            countryInput.send_keys("Chandigarh")
            countryInput.send_keys(Keys.DOWN)
            countryInput.send_keys(Keys.ENTER)
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
            addressInput.send_keys(address)
            time.sleep(3)
            
        def click_continue_button(self):
            continueButton = self.wait.until(EC.presence_of_element_located(self.continue_btn))
            continueButton.click()
            time.sleep(2)