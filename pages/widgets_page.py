import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generator_color
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators
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


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multi_input(self):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            multi_input = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
            multi_input.send_keys(color)
            multi_input.send_keys(Keys.ENTER)
        return colors

    def remove_input(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTIPLE_OUTPUT))
        remove_value = self.elements_are_present(self.locators.REMOVE_CHOSEN_INPUT)
        for value in remove_value:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTIPLE_OUTPUT))
        return count_value_before, count_value_after

    def check_color_multi(self):
        color_list = self.elements_are_present(self.locators.MULTIPLE_OUTPUT)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generator_color()).color_name, k=1)
        single_input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color[0]

    def check_single_color(self):
        color = self.element_is_visible(self.locators.SINGLE_FIELD)
        return color.text
