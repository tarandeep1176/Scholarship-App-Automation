from selenium.webdriver.common.by import By

class AddressPageObjects:
    add_email_btn = (By.CSS_SELECTOR,"[data-test-id='btn-address-contact-email-add']")
    email_input = (By.CSS_SELECTOR,"[data-test-id='input-address-contact-email-0']")
    phone_number_input = (By.CSS_SELECTOR,"[data-test-id='input-address-contact-phone-number-0']")
    whatsapp_number = (By.CSS_SELECTOR,"[data-test-id='input-address-contact-phone-number-1']")
    type_of_housing_dropdown = (By.CSS_SELECTOR,"[data-test-id='btn-select-arrow-addresses-residence-type-of-housing']")
    housing_condition_dropdown = (By.CSS_SELECTOR,"[data-test-id='btn-select-arrow-addresses-residence-housing-condition']")
    country_of_residence_dropdown = (By.CSS_SELECTOR,"[data-test-id='btn-autocomplete-arrow-addresses-residence-country']")
    # country_input = (By.CSS_SELECTOR,"[data-test-id='autocomplete-input-addresses-residence-country']")
    state_dropdown = (By.CSS_SELECTOR,"[data-test-id='btn-autocomplete-arrow-addresses-residence-state']")
    city_of_residency_dropdown = (By.CSS_SELECTOR,"[data-test-id='btn-autocomplete-arrow-addresses-residence-city']")
    dropdown_options = (By.XPATH,"//li[@role='option']")
    zip_code_input = (By.CSS_SELECTOR,"[data-test-id='input-addresses-residence-zip-code']")
    address_input = (By.CSS_SELECTOR,"[data-test-id='input-addresses-residence-address']")
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='btn-continue-address']")