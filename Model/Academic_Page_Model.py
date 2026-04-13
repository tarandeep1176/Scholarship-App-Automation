from pydantic import BaseModel

class AcademicData(BaseModel):
    university: str
    degree: str
    other_expertise: str

class AcademicPageData(BaseModel):
    AcademicData: AcademicData