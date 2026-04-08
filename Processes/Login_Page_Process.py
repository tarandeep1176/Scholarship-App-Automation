from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Data.Login_Page_Data import LoginPageMother

class LoginPageProcess:

    def __init__(self, login:LoginPageFunctions):
        self.login = login

    def run_process(self):
        data = LoginPageMother()
        self.login.select_language(data.language)
        self.login.enter_access_code(data.access_code)
        self.login.submit_access_code()


