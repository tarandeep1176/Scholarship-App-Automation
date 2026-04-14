from Page_Functions.Reference_Page_Functions import ReferencePageFunctions
from Data.Personal_Page_Data import PersonalPageMother

class ReferencePageProcess:

    def __init__(self, reference:ReferencePageFunctions):
        self.reference = reference

    def run_process(self):
        data = PersonalPageMother()
        self.reference.fill_all_references()
        self.reference.click_continue_button()

