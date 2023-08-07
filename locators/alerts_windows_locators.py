from selenium.webdriver.common.by import By


class WindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_TAB_TEXT = (By.ID, "sampleHeading")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")


class AlertsLocators:
    SIMPLE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_BUTTON_5_SECONDS = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    TEXT_SUCCESS = (By.ID, "confirmResult")
    PROMT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMT_RESULT = (By.ID, "promptResult")
