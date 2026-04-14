from faker import Faker
from Model.Employment_Page_Model import EmploymentData, EmploymentPageData

class EmploymentPageMother:
    def __init__(self):
        self.fake = Faker()
        self.institution_name = self.fake.company()
        self.position = self.fake.job()
        self.area = self.fake.catch_phrase()
        self.activity = self.fake.catch_phrase()
        self.monthly_salary = self.fake.random_number(digits=5)
        self.landline_number = self.fake.phone_number()
        self.phone_number = self.fake.phone_number()
        self.zipcode = self.fake.postcode()
        self.address = self.fake.address()
        self.website = self.fake.url()

    def get(self):
        return EmploymentPageData(
            EmploymentData = EmploymentData(
                institution_name = self.institution_name,
                position = self.position,
                area = self.area,
                activity = self.activity,
                monthly_salary = self.monthly_salary,
                landline_number = self.landline_number,
                phone_number = self.phone_number,
                zipcode = self.zipcode,
                address = self.address,
                website = self.website
            )
        )