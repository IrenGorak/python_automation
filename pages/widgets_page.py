from selenium.common import TimeoutException

from locators.widgets_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {"first": {'title': self.locators.SECTION_1,
                               'content': self.locators.CONTENT_SECTION_1},
                     "second": {'title': self.locators.SECTION_2,
                                'content': self.locators.CONTENT_SECTION_2},
                     "third": {'title': self.locators.SECTION_3,
                               'content': self.locators.CONTENT_SECTION_3},
                         }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, section_content]

