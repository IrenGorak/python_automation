import random

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


class DataPickerPageLocators:
    DATA_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    SELECT_DAY = (By.CSS_SELECTOR, "div[class*='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_MONTH_INPUT = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_YEAR_INPUT = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")
    DATE_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgresBarPageLocators:
    PROGRESS_BAR__START_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")


class TabPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    ORIGIN_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    USE_TAB = (By.ID, 'demo-tab-use')
    USE_CONTENT = (By.ID, "demo-tab-use")
    MORE_TABS = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    MORE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")


class ToopTipPageLocators:
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    HOVER_TEXT_BUTTON = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")

    TOOL_TIP_FIELD = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    HOVER_FIELD_TEXT = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")

    TOOL_TIP_TEXT_LINK = (By.XPATH, "//*[.='Contrary']")
    HOVER_TEXT_LINK = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")

    TOOL_TIP_NUMBER_LINK = (By.XPATH, "//*[.='1.10.32']")
    HOVER_NUMBER_TEXT = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")

    TOOP_TIPS_TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")


class SelectMenuPageLocators:
    SELECT_VALUE = (By.CSS_SELECTOR, "div[id='withOptGroup']")
    SELECT_MENU = (By.CSS_SELECTOR, f"div[class=' css-26l3qy-menu']")
    SELECT_MENU_OUTPUT = (By.CSS_SELECTOR, "div[class=' css-1uccc91-singleValue']")
    SELECT_ONE = (By.CSS_SELECTOR, "div[id='selectOne']")
    OLD_STYLE_MENU = (By.CSS_SELECTOR, "select[id='oldSelectMenu']")
