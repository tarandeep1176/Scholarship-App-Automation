from selenium.webdriver.common.by import By

class AdditionalPageObjects:
    facebook_option = (By.XPATH,"//input[@value='FACEBOOK']")
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='btn-continue-additional']")