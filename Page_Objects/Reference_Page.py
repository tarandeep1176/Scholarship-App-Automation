from selenium.webdriver.common.by import By

class ReferencePageObjects:
    ref_dropdown = [(By.CSS_SELECTOR, f'[data-test-id="button-applicant-reference-accordion-{i}"]') for i in range(1,4)]
    ref_first_name = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-first-name-{i}"]') for i in range(1,4)]
    ref_last_name = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-last-name-{i}"]') for i in range(1,4)]
    ref_position = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-position-or-occupation-{i}"]') for i in range(1,4)]
    ref_email = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-email-address-{i}"]') for i in range(1,4)]
    ref_phone_number = [(By.CSS_SELECTOR,f'[data-test-id="input-employment-address-applicant-reference-phone-number-{i}"]') for i in range(1,4)]
    ref_landline_number = [(By.CSS_SELECTOR,f'[data-test-id="input-employment-address-applicant-reference-landline-phone-{i}"]') for i in range(1,4)]
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='btn-continue-references']")