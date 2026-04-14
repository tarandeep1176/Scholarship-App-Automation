from Page_Functions.Employment_Page_Functions import EmploymentPageFunctions
from Data.Employment_Page_Data import EmploymentPageMother

class EmploymentPageProcess:

    def __init__(self, employment:EmploymentPageFunctions):
        self.employment = employment

    def run_process(self):
        data = EmploymentPageMother()
        self.employment.enter_institution_name(data.institution_name)
        self.employment.enter_position(data.position)
        self.employment.enter_area(data.area)
        self.employment.select_worker_category()
        self.employment.enter_activity(data.activity)
        self.employment.select_seniority_in_position()
        self.employment.enter_monthly_salary(data.monthly_salary)
        self.employment.select_country()
        self.employment.select_state()
        self.employment.select_city()
        self.employment.enter_zipcode(data.zipcode)
        self.employment.enter_address(data.address)
        self.employment.enter_landline_number(data.landline_number)
        self.employment.enter_phone_number(data.phone_number)
        self.employment.enter_website(data.website)
        self.employment.click_continue_button()
