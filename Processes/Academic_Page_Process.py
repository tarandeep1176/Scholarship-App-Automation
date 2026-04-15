from Page_Functions.Academic_Page_Functions import AcademicPageFunctions
from Data.Academic_Page_Data import AcademicPageMother

class AcademicPageProcess:

    def __init__(self, academic:AcademicPageFunctions):
        self.academic = academic

    def run_process(self):
        data = AcademicPageMother()
        self.academic.select_educational_level()
        self.academic.enter_university(data.university)
        self.academic.enter_degree(data.degree)
        self.academic.enter_starting_date(data.start_date)
        self.academic.enter_graduation_date(data.grad_date)
        self.academic.select_study_experience()
        self.academic.enter_other_expertise(data.other_expertise)
        self.academic.click_continue_button()
