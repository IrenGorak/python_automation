from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CLASS_NAME, "btn-primary")

    CREATE_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATE_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATE_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATE_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")




