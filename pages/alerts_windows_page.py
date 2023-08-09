import random
import time

from locators.alerts_windows_locators import WindowsPageLocators, AlertsLocators, FrameLocators, NestePageLocators, \
    ModalWindowPageLocators
from pages.base_page import BasePage


class WindowsPage(BasePage):
    locators = WindowsPageLocators()

    def check_open_new_tab(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return text_title

    def check_open_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).lick()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT_BUTTON).click()
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        finally:
            alert_window = self.driver.switch_to.alert
            alert_window.accept()

    def check_alert_5_seconds(self):
        self.element_is_visible(self.locators.ALERT_BUTTON_5_SECONDS).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        finally:
            alert_window = self.driver.switch_to.alert
            alert_window.accept()

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        try:
            alert_window = self.driver.switch_to.alert
            choice = random.choice([0, 1])
            if choice == 0:
                alert_window.dismiss()
            else:
                alert_window.accept()
        finally:
            text_result = self.element_is_present(self.locators.TEXT_SUCCESS).text
            print(text_result)
        return text_result

    def check_promt_alert(self):
        text = f"autotest{random.randint(1, 32)}"
        self.element_is_visible(self.locators.PROMT_BUTTON).click()
        try:
            alert_window = self.driver.switch_to.alert
            alert_window.send_keys(text)
            alert_window.accept()
        finally:
            text_result = self.element_is_present(self.locators.PROMT_RESULT).text
            print(text_result)
        return text, text_result


class FramePage(BasePage):
    locators = FrameLocators()

    def check_frames(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FRAME_1)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == "frame2":
            frame = self.element_is_present(self.locators.FRAME_2)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]


class NestedFramePage(BasePage):
    locators = NestePageLocators()

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.MAIN_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.MAIN_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalWindowPage(BasePage):
    locators = ModalWindowPageLocators()

    def check_small_modaL_window(self):
        self.element_is_visible(self.locators.SMALL_MODAL_WINDOW).click()
        title__small_window = self.element_is_visible(self.locators.SMALL_TITLE).text
        body_small_window = self.element_is_visible(self.locators.SMALL_BODY).text
        self.driver.switch_to.default_content()
        return title__small_window, len(body_small_window)

    def check_large_modaL_window(self):
        self.element_is_visible(self.locators.LARGE_MODAL_WINDOW).click()
        title_large_window = self.element_is_visible(self.locators.LARGE_TITLE).text
        body_large_window = self.element_is_visible(self.locators.LARGE_BODY).text
        return title_large_window, len(body_large_window)
