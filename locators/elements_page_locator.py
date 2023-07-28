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


class CheckBoxPageLocators:
    EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEM = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    SUCCESS_OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonLocators:
    YES_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='impressiveRadio']")
    NO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='noRadio']")
    OUTPUT_RESULT = (By.CLASS_NAME, "text-success")


class WebTablePageLocators:
    ADD_NEW_PERSON_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    USER_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    USER_AGE = (By.ID, "age")
    USER_SALARY = (By.ID, "salary")
    USER_DEPARTMENT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")

    PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_FIELD = (By.ID, "searchBox")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")

    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    NO_ROWS_DATA = (By.CLASS_NAME, "rt-noData")
    SELECT_ROWS = (By.CLASS_NAME, "select-wrap")
