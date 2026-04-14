from pydantic import BaseModel

class EmploymentData(BaseModel):
    institution_name: str
    position: str
    area: str
    activity: str
    monthly_salary: str
    landline_number: str
    phone_number: str
    zipcode: str
    address: str

class EmploymentPageData(BaseModel):
    EmploymentData: EmploymentData