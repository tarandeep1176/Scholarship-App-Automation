from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Welcome_Page import WelcomePageObjects
import time


class WelcomePageFunctions(WelcomePageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15) 

        def check_snackbar_message(self):
            try:
                snackbar = self.wait.until(EC.visibility_of_element_located(self.snackbar_message))
                actual_message = snackbar.text
                actual_message == "Login successful"
                print("Snack-Bar message Extracted as: " + actual_message)
            except:
                print("No Snackbar Encountered.")
                
        def check_welcome_message(self):
            try:
                welcomeMessage = self.wait.until(EC.visibility_of_element_located(self.welcome_message))
                actual_message = welcomeMessage.text
                print("Welcome message Extracted as: " + actual_message)
            except:
                print("No Welcome Message Encountered.")

        def click_get_started(self):
            try:
                getStartedButton = self.wait.until(EC.visibility_of_element_located(self.get_started_btn))
                time.sleep(2)
                getStartedButton.click()
                time.sleep(4)
                
            except:
                print("Already logged in.")
                