from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Welcome_Page import WelcomePageObjects
import time


class WelcomePageFunctions(WelcomePageObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15) 

        def click_get_started(self):
            try:
                getStartedButton = self.wait.until(EC.visibility_of_element_located(self.get_started_btn))
                getStartedButton.click()
                time.sleep(3)
                
            except:
                print("Already logged in.")
                