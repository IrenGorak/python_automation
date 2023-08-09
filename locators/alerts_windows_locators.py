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


class FrameLocators:
    FRAME_1 = (By.ID, "frame1")
    FRAME_2 = (By.ID, "frame2")
    TITLE_FRAME = (By.ID, "sampleHeading")


class NestePageLocators:
    MAIN_FRAME = (By.ID, "frame1")
    MAIN_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalWindowPageLocators:
    SMALL_MODAL_WINDOW = (By.ID, "showSmallModal")
    SMALL_CLOSED_BUTTON = (By.ID, "closeSmallModal")
    SMALL_TITLE = (By.ID, "example-modal-sizes-title-sm")
    SMALL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")

    LARGE_MODAL_WINDOW = (By.ID, "showLargeModal")
    LARGE_CLOSE_BUTTON = (By.ID, "closeLargeModal")
    LARGE_TITLE = (By.ID, "example-modal-sizes-title-lg")
    LARGE_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
