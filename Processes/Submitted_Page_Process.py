from Page_Functions.Submitted_Page_Functions import SubmittedPageFunctions

class SubmittedPageProcess:

    def __init__(self, submitted:SubmittedPageFunctions):
        self.submitted = submitted

    def run_process(self):
        self.submitted.check_submitted_text()

