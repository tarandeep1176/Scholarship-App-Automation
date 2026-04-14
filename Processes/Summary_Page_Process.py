from Page_Functions.Summary_Page_Functions import SummaryPageFunctions

class SummaryPageProcess:

    def __init__(self, summary:SummaryPageFunctions):
        self.summary = summary

    def run_process(self):
        self.summary.click_terms_and_conditions_checkbox()
        self.summary.click_submit_button()
