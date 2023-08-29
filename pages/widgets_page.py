import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generator_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators, \
    SliderPageLocators, ProgresBarPageLocators, TabPageLocators, ToopTipPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
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


class DataPickerPage(BasePage):
    locators = DataPickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATA_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.SELECT_MONTH, date.month)
        self.select_date_by_text(self.locators.SELECT_YEAR, date.year)
        self.select_date_item_from_list(self.locators.SELECT_DAY, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_MONTH_INPUT).click()
        self.select_date_item_from_list(self.locators.MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_YEAR_INPUT).click()
        self.select_date_item_from_list(self.locators.YEAR_LIST, "2020")
        self.select_date_item_from_list(self.locators.SELECT_DAY, date.day)
        self.select_date_item_from_list(self.locators.DATE_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgresBarPage(BasePage):
    locators = ProgresBarPageLocators()

    def check_progress_bar(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR__START_BUTTON)
        progress_bar.click()
        time.sleep(random.randint(2, 8))
        progress_bar.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabPage(BasePage):
    locators = TabPageLocators()

    def check_open_tab(self, name_tab):
        tabs = {
                "what":
                    {'title': self.locators.WHAT_TAB,
                     'content': self.locators.WHAT_CONTENT},
                "origin":
                    {'title': self.locators.ORIGIN_TAB,
                     'content': self.locators.ORIGIN_CONTENT},
                "use":
                    {'title': self.locators.USE_TAB,
                     'content': self.locators.USE_CONTENT},
             }

        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(content)


class ToopTipPage(BasePage):
    locators = ToopTipPageLocators()

    def get_the_text_from_tool_tips(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        time.sleep(0.5)
        self.element_is_visible(wait_element)
        tool_tip_text = self.element_is_visible(self.locators.TOOP_TIPS_TEXT)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_the_text_from_tool_tips(self.locators.TOOL_TIP_BUTTON,
                                                                self.locators.HOVER_TEXT_BUTTON)
        tool_tip_text_field = self.get_the_text_from_tool_tips(self.locators.TOOL_TIP_FIELD,
                                                               self.locators.HOVER_FIELD_TEXT)
        tool_tip_text_link = self.get_the_text_from_tool_tips(self.locators.TOOL_TIP_TEXT_LINK,
                                                              self.locators.HOVER_TEXT_LINK)
        tool_tip_text_number = self.get_the_text_from_tool_tips(self.locators.TOOL_TIP_NUMBER_LINK,
                                                                self.locators.HOVER_NUMBER_TEXT)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_link, tool_tip_text_number


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def check_select_menu(self):
        self.element_is_visible(self.locators.SELECT_VALUE).click()
        self.element_is_present(self.locators.SELECT_MENU).click()
        output_select_value = self.element_is_visible(self.locators.SELECT_MENU_OUTPUT).text

        self.element_is_visible(self.locators.SELECT_ONE).click()
        self.element_is_present(self.locators.SELECT_MENU).click()
        output_select_one = self.element_is_visible(self.locators.SELECT_MENU_OUTPUT).text

        color = random.sample(next(generator_color()).color_name, k=1)
        output_old_style = self.element_is_visible(self.locators.OLD_STYLE_MENU)
        output_old_style.send_keys(color)
        output_old_style.send_keys(Keys.ENTER)
        self.driver.back()
        return output_select_value, output_select_one, output_old_style

