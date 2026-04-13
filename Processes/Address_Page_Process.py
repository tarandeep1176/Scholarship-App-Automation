from Page_Functions.Address_Page_Functions import AddressPageFunctions
from Data.Address_Page_Data import AddressPageMother

class AddressPageProcess:

    def __init__(self, address:AddressPageFunctions):
        self.address = address

    def run_process(self):
        data = AddressPageMother()
        self.address.click_add_email()
        self.address.enter_email(data.email)
        self.address.enter_mobile_number(data.mobile_number)
        self.address.enter_whatsapp_number(data.whatsapp_number)
        self.address.select_type_of_housing()
        self.address.select_housing_condition()
        self.address.select_country()
        self.address.enter_zipcode(data.zipcode)
        self.address.enter_address(data.address)
        self.address.click_continue_button()
