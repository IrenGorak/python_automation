import os
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_all_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.USER_EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.USER_GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.phone)
        self.element_is_visible(self.locators.SUBJECTS).send_keys("Maths")
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.PICTURE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        return person
