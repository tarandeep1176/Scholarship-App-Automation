from pydantic import BaseModel

class AddressData(BaseModel):
    email: str
    mobile_number: str
    whatsapp_number: str
    zipcode: str
    address: str

class AddressPageData(BaseModel):
    AddressData: AddressData