from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Personal_Page import PersonalPageObjects
from selenium.webdriver.common.keys import Keys
import time
import random

class PersonalPageFunctions(PersonalPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)
                
        def select_document_type(self):
            documentDropdown = self.wait.until(EC.presence_of_element_located(self.type_of_document_dropdown))
            documentDropdown.click()
            time.sleep(2)
            options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
            random_option = random.choice(options)
            random_option.click()
            
        def enter_document_number(self,doc_number):
            documentNumber = self.wait.until(EC.presence_of_element_located(self.document_number))
            documentNumber.click()
            time.sleep(2)
            documentNumber.send_keys(Keys.CONTROL + "a")
            documentNumber.send_keys(Keys.DELETE)
            time.sleep(3)
            documentNumber.send_keys(doc_number)
            
        def select_marital_status(self):
            maritalStatusDropdown = self.wait.until(EC.presence_of_element_located(self.marital_status_dropdown))
            maritalStatusDropdown.click()
            time.sleep(2)
            options = self.wait.until(EC.presence_of_all_elements_located(self.dropdown_options))
            random_option = random.choice(options)
            random_option.click()
            
        def enter_profession(self,profession):
            professionInput = self.wait.until(EC.presence_of_element_located(self.profession_input))
            professionInput.click()
            time.sleep(3)
            professionInput.send_keys(Keys.CONTROL + "a")
            professionInput.send_keys(Keys.DELETE)
            time.sleep(2)
            professionInput.send_keys(profession)
            
        def enter_date_of_birth(self,dob):
            dobInput = self.wait.until(EC.presence_of_element_located(self.dob_input))
            dobInput.click()
            time.sleep(2)
            dobInput.send_keys(dob)
            
        def select_country(self):
            country = self.wait.until(EC.visibility_of_element_located(self.country_dropdown))
            time.sleep(3)
            country.click()
            time.sleep(3)
            countryInput = self.wait.until(EC.visibility_of_element_located(self.country_input))
            countryInput.send_keys("India")
            countryInput.send_keys(Keys.DOWN)
            countryInput.send_keys(Keys.DOWN)
            countryInput.send_keys(Keys.ENTER)
            time.sleep(3)
            
        def select_state(self):
            state = self.wait.until(EC.visibility_of_element_located(self.state_dropdown))
            time.sleep(3)
            state.click()
            time.sleep(3)
            stateInput = self.wait.until(EC.visibility_of_element_located(self.state_input))
            stateInput.send_keys("Chandigarh")
            stateInput.send_keys(Keys.DOWN)
            stateInput.send_keys(Keys.ENTER)
            time.sleep(3)
            
        def select_city(self):
            city = self.wait.until(EC.visibility_of_element_located(self.city_dropdown))
            time.sleep(3)
            city.click()
            time.sleep(3)
            cityInput = self.wait.until(EC.visibility_of_element_located(self.city_input))
            cityInput.send_keys("Chandigarh")
            cityInput.send_keys(Keys.DOWN)
            cityInput.send_keys(Keys.ENTER)
            time.sleep(3)
            
        def select_nationality(self):
            nationality = self.wait.until(EC.visibility_of_element_located(self.nationality_dropdown))
            time.sleep(3)
            nationality.click()
            time.sleep(3)
            nationalityInput = self.wait.until(EC.visibility_of_element_located(self.nationality_input))
            nationalityInput.send_keys("India")
            nationalityInput.send_keys(Keys.DOWN)
            nationalityInput.send_keys(Keys.DOWN)
            nationalityInput.send_keys(Keys.ENTER)
            time.sleep(3)
            
        def enter_monthly_income(self,monthly_income):
            monthlyIncomeInput = self.wait.until(EC.presence_of_element_located(self.monthly_income_input))
            monthlyIncomeInput.click()
            time.sleep(2)
            monthlyIncomeInput.send_keys(Keys.CONTROL + "a")
            monthlyIncomeInput.send_keys(Keys.DELETE)
            time.sleep(2)
            monthlyIncomeInput.send_keys(monthly_income)
            
        def enter_monthly_expense(self,monthly_expense):
            monthlyExpenseInput = self.wait.until(EC.presence_of_element_located(self.monthly_expense_input))
            monthlyExpenseInput.click()
            time.sleep(2)
            monthlyExpenseInput.send_keys(Keys.CONTROL + "a")
            monthlyExpenseInput.send_keys(Keys.DELETE)
            time.sleep(2)
            monthlyExpenseInput.send_keys(monthly_expense)
            
        def select_financially_dependent(self):
            financiallyDependent = self.wait.until(EC.presence_of_element_located(self.financially_dependent))
            financiallyDependent.click()
            time.sleep(2)
            
        def select_has_children(self):
            hasChildren = self.wait.until(EC.presence_of_element_located(self.has_children))
            hasChildren.click()
            time.sleep(2)
            childrenAge = self.wait.until(EC.presence_of_element_located(self.children_age))
            childrenAge.click()
            time.sleep(3)
            childrenAge.send_keys("15")
            
        def click_continue_button(self):
            continueButton = self.wait.until(EC.presence_of_element_located(self.continue_btn))
            continueButton.click()
            time.sleep(2)