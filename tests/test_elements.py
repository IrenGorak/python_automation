import time

from pages.elemets_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElement:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.remove_footer()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, "the full_name doesn't match with expected result"
            assert email == output_email, "the email doesn't match with expected result"
            assert current_address == output_current_address, "the current_address doesn't match with expected result"
            assert permanent_address == output_permanent_address, "the permanent_address doesn't match with expected result"

            """
            OR
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data
            """
    class TestCheckbox:
        def test_check_checkbox(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_checkbox_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, "Checkboxes have not been selected"
            time.sleep(3)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "yes have not been selected"
            assert output_no == "No", "no have not been selected"
            assert output_impressive == "Impressive", "impressive have not been selected"
