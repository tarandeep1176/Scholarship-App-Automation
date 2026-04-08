from selenium.webdriver.common.by import By

class LoginPageObjects:
    language_dropdown = (By.CSS_SELECTOR,"[data-test-id='select-language']")
    english_language = (By.CSS_SELECTOR,"[data-test-id='li-en-US-language']")
    spanish_language = (By.CSS_SELECTOR,"[data-test-id='li-es-ES-language']")
    access_code_input = (By.CSS_SELECTOR,"[data-test-id='input-login-access-code']")
    submit_btn = (By.CSS_SELECTOR,"[data-test-id='btn-submit-login']")