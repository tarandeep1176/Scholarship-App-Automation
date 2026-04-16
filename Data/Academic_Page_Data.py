from faker import Faker
from Model.Academic_Page_Model import AcademicData, AcademicPageData

class AcademicPageMother:
    def __init__(self):
        self.fake = Faker()
        self.university = self.fake.company()
        self.degree = self.fake.job()
        start = self.fake.date_between(start_date='-10y', end_date='-5y')
        grad = self.fake.date_between(start_date=start, end_date='today')
        self.start_date = start.strftime("%m/%Y")
        self.grad_date = grad.strftime("%m/%Y")
        self.other_expertise = self.fake.catch_phrase()
        
    def get(self):
        return AcademicPageData(
            AcademicData = AcademicData(
                university = self.university,
                degree = self.degree,
                start_date = self.start_date,
                grad_date = self.grad_date,
                other_expertise = self.other_expertise
            )
        )