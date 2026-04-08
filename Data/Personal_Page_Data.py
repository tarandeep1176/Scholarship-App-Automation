import dotenv
import os
from faker import Faker
from Model.Personal_Page_Model import PersonalData, PersonalPageData

class PersonalPageMother:
    def __init__(self):
        self.fake = Faker()
        self.document_number = self.fake.bothify(text='#########')
        self.profession = self.fake.job()
        self.date_of_birth = self.fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%m/%d/%Y")
        self.monthly_income = self.fake.random_number(digits=5)
        self.monthly_expense= self.fake.random_number(digits=5)
        
    def get(self):
        return PersonalPageData(
            PersonalData = PersonalData(
                document_number = self.document_number,
                profession = self.profession,
                date_of_birth = self.date_of_birth,
                monthly_income = self.monthly_income,
                monthly_expense = self.monthly_expense
        )
    )