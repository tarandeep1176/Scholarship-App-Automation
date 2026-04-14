from Page_Functions.Documents_Page_Functions import DocumentsPageFunctions

class DocumentsPageProcess:

    def __init__(self, documents:DocumentsPageFunctions):
        self.documents = documents

    def run_process(self):
        self.documents.upload_passport()
        self.documents.upload_curriculum_vitae()
        self.documents.upload_letter_of_motive()
        self.documents.upload_other_document()
        self.documents.upload_degree()
        self.documents.click_continue_button()
