import dotenv
import os
from Model.Login_Page_Model import LoginData, AccessCodeData, LanguageData

class LoginPageMother:
    def __init__(self):
        dotenv.load_dotenv()
        self.access_code = os.getenv("ACCESS_CODE")
        self.language = os.getenv("LANGUAGE")
        
    def get(self):
        return LoginData(
            AccessCodeData = AccessCodeData(username = self.access_code),
            LanguageData = LanguageData(language = self.language)
        )