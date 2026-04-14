from selenium.webdriver.common.by import By

class DocumentsPageObjects:
    passport_upload_btn = (By.CSS_SELECTOR,"[data-test-id='upload-btn-documents-id/passport']")
    passport_upload_input = (By.CSS_SELECTOR,"[data-test-id='input-documents-id/passport']")
    curriculum_vitae_upload_btn = (By.CSS_SELECTOR,"[data-test-id='upload-btn-documents-curriculum-vitae']")
    curriculum_vitae_upload_input = (By.CSS_SELECTOR,"[data-test-id='input-documents-curriculum-vitae']")
    letter_of_motive_upload_btn = (By.CSS_SELECTOR,"[data-test-id='upload-btn-documents-letter-of-motive']")
    letter_of_motive_upload_input = (By.CSS_SELECTOR,"[data-test-id='input-documents-letter-of-motive']")
    other_upload_btn = (By.CSS_SELECTOR,"[data-test-id='upload-btn-documents-other']")
    other_upload_input = (By.CSS_SELECTOR,"[data-test-id='input-documents-other']")
    degree_upload_btn = (By.CSS_SELECTOR,"[data-test-id='upload-btn-documents-degree']")
    degree_upload_input = (By.CSS_SELECTOR,"[data-test-id='input-documents-degree']")
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='btn-continue-documents']")