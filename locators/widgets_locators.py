from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_1 = (By.ID, "section1Heading")
    CONTENT_SECTION_1 = (By.ID, "section1Content")
    SECTION_2 = (By.ID, "section2Heading")
    CONTENT_SECTION_2 = (By.ID, "section2Content")
    SECTION_3 = (By.ID, "section3Heading")
    CONTENT_SECTION_3 = (By.ID, "section3Content")


class AutoCompletePageLocators:
    MULTIPLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTIPLE_OUTPUT = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    REMOVE_CHOSEN_INPUT = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"]')
    SINGLE_FIELD = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
