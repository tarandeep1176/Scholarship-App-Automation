from selenium.webdriver.common.by import By

class WelcomePageObjects:
    snackbar_message = (By.CSS_SELECTOR,"[data-test-id='text-Applicant-Logged-in']")
    welcome_message = (By.CSS_SELECTOR,"[data-test-id='text-welcome-message']")
    get_started_btn = (By.CSS_SELECTOR,"[data-test-id='btn-get-started-welcome']")
