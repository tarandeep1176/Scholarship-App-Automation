from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Login_Page import LoginPageObjects
import time


class LoginPageFunctions(LoginPageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def select_language(self,language):
            languageDropdown = self.wait.until(EC.presence_of_element_located(self.language_dropdown))
            languageDropdown.click()
            time.sleep(2)
            if(language == "Inglés (Estados Unidos)" or language == "English (United States)"):
                englishLanguage = self.wait.until(EC.visibility_of_element_located(self.english_language))
                englishLanguage.click()
            else:
                spanishLanguage = self.wait.until(EC.visibility_of_element_located(self.spanish_language))
                spanishLanguage.click()
            time.sleep(2)  

        def enter_access_code(self,access_code):
                time.sleep(1)
                accessCodeInput = self.wait.until(EC.visibility_of_element_located(self.access_code_input))
                accessCodeInput.click()
                time.sleep(2)
                accessCodeInput.send_keys(access_code)
                time.sleep(3)
                
        def submit_access_code(self):
                submitButton = self.driver.find_element(*self.submit_btn)
                submitButton.click()
                time.sleep(3)
