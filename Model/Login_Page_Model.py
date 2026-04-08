from pydantic import BaseModel

class AccessCodeData(BaseModel):
    access_code : str

class LanguageData(BaseModel):
    language : str
    
class LoginData(BaseModel):
    AccessCodeData : AccessCodeData
    LanguageData : LanguageData