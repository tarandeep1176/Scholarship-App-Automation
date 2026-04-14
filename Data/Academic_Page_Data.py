from faker import Faker
from Model.Academic_Page_Model import AcademicData, AcademicPageData

class AcademicPageMother:
    def __init__(self):
        self.fake = Faker()
        self.university = self.fake.company()
        self.degree = self.fake.job()
        self.other_expertise = self.fake.catch_phrase()
        
    def get(self):
        return AcademicPageData(
            AcademicData = AcademicData(
                university = self.university,
                degree = self.degree,
                other_expertise = self.other_expertise
            )
        )