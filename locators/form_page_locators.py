import random
from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    USER_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    USER_GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1,3)}']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    BIRTH_DATA = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1,3)}']")
    PICTURE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.ID, "state")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.ID, "'city")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id=react-select-4-input")
    SUBMIT = (By.CSS_SELECTOR, "button[id=submit']")
