from Libraries.Libraries import Import_libraries
from Data.Config_Data import ConfigData
from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Page_Functions.Welcome_Page_Functions import WelcomePageFunctions
from Page_Functions.Personal_Page_Functions import PersonalPageFunctions
from Page_Functions.Address_Page_Functions import AddressPageFunctions
from Page_Functions.Academic_Page_Functions import AcademicPageFunctions
from Page_Functions.Employment_Page_Functions import EmploymentPageFunctions
from Page_Functions.Reference_Page_Functions import ReferencePageFunctions
from Page_Functions.Documents_Page_Functions import DocumentsPageFunctions
from Page_Functions.Additional_Page_Functions import AdditionalPageFunctions
from Page_Functions.Summary_Page_Functions import SummaryPageFunctions
from Page_Functions.Submitted_Page_Functions import SubmittedPageFunctions

from Processes.Login_Page_Process import LoginPageProcess
from Processes.Welcome_Page_Process import WelcomePageProcess
from Processes.Personal_Page_Process import PersonalPageProcess
from Processes.Address_Page_Process import AddressPageProcess
from Processes.Academic_Page_Process import AcademicPageProcess
from Processes.Employment_Page_Process import EmploymentPageProcess
from Processes.Reference_Page_Process import ReferencePageProcess
from Processes.Documents_Page_Process import DocumentsPageProcess
from Processes.Additional_Page_Process import AdditionalPageProcess
from Processes.Summary_Page_Process import SummaryPageProcess
from Processes.Submitted_Page_Process import SubmittedPageProcess

data = ConfigData()
driver = Import_libraries.get_driver()
driver.get(data.BASE_URL)
print("BASE_URL:", repr(data.BASE_URL))

login_page_functions = LoginPageFunctions(driver)
welcome_page_functions = WelcomePageFunctions(driver)
personal_page_functions = PersonalPageFunctions(driver)
address_page_functions = AddressPageFunctions(driver)
academic_page_functions = AcademicPageFunctions(driver)
employment_page_functions = EmploymentPageFunctions(driver)
reference_page_functions = ReferencePageFunctions(driver)
documents_page_functions = DocumentsPageFunctions(driver)
additional_page_functions = AdditionalPageFunctions(driver)
summary_page_functions = SummaryPageFunctions(driver)
submitted_page_functions = SubmittedPageFunctions(driver)

def test_login_page():
    login = LoginPageProcess(login_page_functions)
    login.run_process()

def test_welcome_page():
    phone = WelcomePageProcess(welcome_page_functions)
    phone.run_process()

def test_personal_page():
    personal = PersonalPageProcess(personal_page_functions)
    personal.run_process()

def test_address_page():
    address = AddressPageProcess(address_page_functions)
    address.run_process()
    
def test_academic_page():
    academic = AcademicPageProcess(academic_page_functions)
    academic.run_process()
    
def test_Employment_page():
    employment = EmploymentPageProcess(employment_page_functions)
    employment.run_process()
    
def test_Reference_page():
    reference = ReferencePageProcess(reference_page_functions)
    reference.run_process()
    
def test_Documents_page():
    documents = DocumentsPageProcess(documents_page_functions)
    documents.run_process()
    
def test_Additional_page():
    additional = AdditionalPageProcess(additional_page_functions)
    additional.run_process()
    
def test_Summary_page():
    summary = SummaryPageProcess(summary_page_functions)
    summary.run_process()
    
def test_Submitted_page():
    submitted = SubmittedPageProcess(submitted_page_functions)
    submitted.run_process()