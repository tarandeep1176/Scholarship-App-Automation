from pydantic import BaseModel

class PersonalData(BaseModel):
    document_number: str
    profession: str
    date_of_birth: str
    monthly_income: str
    monthly_expense: str

class PersonalPageData(BaseModel):
    PersonalData: PersonalData