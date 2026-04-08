from Libraries.Libraries import Import_libraries
from Data.Config_Data import ConfigData
from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Page_Functions.Welcome_Page_Functions import WelcomePageFunctions
from Page_Functions.Personal_Page_Functions import PersonalPageFunctions

from Processes.Login_Page_Process import LoginPageProcess
from Processes.Welcome_Page_Process import WelcomePageProcess
from Processes.Personal_Page_Process import PersonalPageProcess

data = ConfigData()
driver = Import_libraries.get_driver()
driver.get(data.BASE_URL)
print("BASE_URL:", repr(data.BASE_URL))

login_page_functions = LoginPageFunctions(driver)
welcome_page_functions = WelcomePageFunctions(driver)
personal_page_functions = PersonalPageFunctions(driver)

def test_login():
    login = LoginPageProcess(login_page_functions)
    login.run_process()

def test_welcome():
    phone = WelcomePageProcess(welcome_page_functions)
    phone.run_process()

def test_personal():
    checkout = PersonalPageProcess(personal_page_functions)
    checkout.run_process()
