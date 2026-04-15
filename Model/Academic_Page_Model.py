from pydantic import BaseModel

class AcademicData(BaseModel):
    university: str
    degree: str
    start_date: str
    grad_date: str
    other_expertise: str

class AcademicPageData(BaseModel):
    AcademicData: AcademicData