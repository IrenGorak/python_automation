import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locator import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATE_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATE_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATE_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATE_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_checkbox_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEM)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, ".//ancestor::span[@class='rct-text']")
            data.append(title_item.text)
        return str(data).replace(" ", '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.SUCCESS_OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return  str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_on_the_button(self, choice):
        choices = {'yes': self.locators.YES_BUTTON,
                   'impressive': self.locators.IMPRESSIVE_BUTTON,
                   'no': self.locators.NO_BUTTON}

        radio = self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_NEW_PERSON_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.USER_EMAIL).send_keys(email)
            self.element_is_visible(self.locators.USER_AGE).send_keys(age)
            self.element_is_visible(self.locators.USER_SALARY).send_keys(salary)
            self.element_is_visible(self.locators.USER_DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.PERSON_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_person_in_table(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    def check_the_search_result(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]")
        return row.text.splitlines()
