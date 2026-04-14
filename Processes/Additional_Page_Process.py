from Page_Functions.Additional_Page_Functions import AdditionalPageFunctions

class AdditionalPageProcess:

    def __init__(self, additional:AdditionalPageFunctions):
        self.additional = additional

    def run_process(self):
        self.additional.select_additional_option()
        self.additional.click_continue_button()