from faker import Faker
from Model.Address_Page_Model import AddressData, AddressPageData

class AddressPageMother:
    def __init__(self):
        self.fake = Faker()
        self.email = self.fake.email()
        self.mobile_number = self.fake.phone_number()
        self.whatsapp_number = self.fake.phone_number()
        self.zipcode = self.fake.postcode()
        self.address = self.fake.street_address()
        
    def get(self):
        return AddressPageData(
            AddressData = AddressData(
                email = self.email,
                mobile_number = self.mobile_number,
                whatsapp_number = self.whatsapp_number,
                zipcode = self.zipcode,
                address = self.address
            )
        )