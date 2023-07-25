
from pages.elemets_page import TextBoxPage


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

