from Libraries.Libraries import Import_libraries
from Data.Config_Data import ConfigData
from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Page_Functions.Welcome_Page_Functions import WelcomePageFunctions
from Page_Functions.Personal_Page_Functions import PersonalPageFunctions
from Page_Functions.Address_Page_Functions import AddressPageFunctions
from Page_Functions.Academic_Page_Functions import AcademicPageFunctions

from Processes.Login_Page_Process import LoginPageProcess
from Processes.Welcome_Page_Process import WelcomePageProcess
from Processes.Personal_Page_Process import PersonalPageProcess
from Processes.Address_Page_Process import AddressPageProcess
from Processes.Academic_Page_Process import AcademicPageProcess

data = ConfigData()
driver = Import_libraries.get_driver()
driver.get(data.BASE_URL)
print("BASE_URL:", repr(data.BASE_URL))

login_page_functions = LoginPageFunctions(driver)
welcome_page_functions = WelcomePageFunctions(driver)
personal_page_functions = PersonalPageFunctions(driver)
address_page_functions = AddressPageFunctions(driver)
academic_page_functions = AcademicPageFunctions(driver)

def test_login():
    login = LoginPageProcess(login_page_functions)
    login.run_process()

def test_welcome():
    phone = WelcomePageProcess(welcome_page_functions)
    phone.run_process()

def test_personal():
    personal = PersonalPageProcess(personal_page_functions)
    personal.run_process()

def test_address():
    address = AddressPageProcess(address_page_functions)
    address.run_process()
    
def test_Academic():
    academic = AcademicPageProcess(academic_page_functions)
    academic.run_process()