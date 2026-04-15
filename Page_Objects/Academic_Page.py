from selenium.webdriver.common.by import By

class AcademicPageObjects:
    educational_level_dropdown = (By.CSS_SELECTOR,"[data-test-id='btn-select-arrow-academic-education-level-1']")
    dropdown_options = (By.XPATH,"//li[@role='option']")
    university_input = (By.CSS_SELECTOR,"[data-test-id='input-academic-education-institution-1']")
    degree_input = (By.CSS_SELECTOR,"[data-test-id='input-academic-education-degree-1']")
    starting_date = (By.CSS_SELECTOR,"[data-test-id='date-picker-input-academic-education-start-date-1']")
    graduation_date = (By.CSS_SELECTOR,"[data-test-id='date-picker-input-academic-education-graduation-date-1']")
    online_study_mode = (By.CSS_SELECTOR,"[data-test-id='radio-input-academic-online-study-experience-no']")
    training_checkbox = (By.CSS_SELECTOR,"[data-test-id='UNIVERSITY_TRAINING_unchecked-icon']")
    other_expertise = (By.CSS_SELECTOR,"[data-test-id='input-academic-other-expertise']")
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='btn-continue-academic']")