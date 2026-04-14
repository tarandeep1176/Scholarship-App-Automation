from selenium.webdriver.common.by import By

class SummaryPageObjects:
    terms_and_conditions_checkbox = (By.CSS_SELECTOR,"[data-test-id='input-checkbox-terms-and-conditions']")
    submit_btn = (By.CSS_SELECTOR,"[data-test-id='btn-send-summary']")