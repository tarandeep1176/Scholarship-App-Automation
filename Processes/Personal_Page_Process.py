from Page_Functions.Personal_Page_Functions import PersonalPageFunctions
from Data.Personal_Page_Data import PersonalPageMother

class PersonalPageProcess:

    def __init__(self, personal:PersonalPageFunctions):
        self.personal = personal

    def run_process(self):
        data = PersonalPageMother()
        self.personal.select_document_type()
        self.personal.enter_document_number(data.document_number)
        self.personal.select_marital_status()
        self.personal.enter_profession(data.profession)
        self.personal.enter_date_of_birth(data.date_of_birth)
        self.personal.select_country_personal()
        self.personal.select_state_personal()
        self.personal.select_city_personal()
        self.personal.select_nationality()
        self.personal.enter_monthly_income(data.monthly_income)
        self.personal.enter_monthly_expense(data.monthly_expense)
        self.personal.select_financially_dependent()
        self.personal.select_has_children()
        self.personal.click_continue_button()


