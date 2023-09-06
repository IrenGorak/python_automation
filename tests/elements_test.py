import random
import time
from pages.elemets_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinkPage, \
    UploadDownloadPage, DynamicPropertiesPage


class TestElement:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.remove_footer()
            full_name, email, current_address, permanent_addr = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full_name doesn't match with expected result"
            assert email == output_email, "the email doesn't match with expected result"
            assert current_address == output_current_address, "the current_address doesn't match with expected result"
            assert permanent_addr == output_permanent_addr, "the permanent_address doesn't match with expected result"

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
            assert input_checkbox == output_result, "Checkboxes have not selected"
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
            assert output_yes == "Yes", "yes have not selected"
            assert output_no == "No", "no have not selected"
            assert output_impressive == "Impressive", "impressive have not selected"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            input_new_person = web_table_page.add_new_person()
            output_table = web_table_page.check_new_added_person()
            assert input_new_person in output_table, "the new person has not in table"
            time.sleep(4)

        def test_search_person_in_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person_in_table(key_word)
            table_result = web_table_page.check_the_search_result()
            print(key_word)
            print(table_result)
            assert key_word in table_result, "the resul not find in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_person_in_table(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_the_search_result()
            assert age in row, "the age not changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person_in_table(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found"

        # the bug found in the page, so the test failed.
        # When nwe change the rows in pages we don't see dropdown for selected page
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.change_rows_count()
            assert count == [5, 10], "The number of rows in the table has not been change"

    class TestButtonPage:
        def test_different_click_on_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', "The double button not pressed"
            assert right == 'You have done a right click', "The right button not pressed"
            assert click == 'You have done a dynamic click', "The dynamic button not pressed"

    class TestLinkPage:
        def test_the_correct_link(self, driver):
            link_page = LinkPage(driver, "https://demoqa.com/links")
            link_page.open()
            href_link, current_url = link_page.check_new_tab_simple_link()
            print(href_link, current_url)
            assert href_link == current_url

        def test_broken_link(self, driver):
            link_page = LinkPage(driver, "https://demoqa.com/links")
            link_page.open()
            response_code = link_page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400

    class TestUploadDownload:
        def test_upload_file(self, driver):
            upload_file = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_file.open()
            upload_file.upload_file()

        def test_download_file(self, driver):
            download_file = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            download_file.open()
            check = download_file.download_file()
            assert check is True, "The file has not downloaded"

    class TestDynamicProperties:
        def test_change_color_button(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties.open()
            color_before, color_after = dynamic_properties.check_change_color()
            assert color_before != color_after, "The color not changed"

        def test_visible_after_button(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties.open()
            appear = dynamic_properties.check_appear_button()
            assert appear is True, "The button not visible after 5 second"

        def test_check_enable_button(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties.open()
            enable = dynamic_properties.check_enable_button()
            assert enable is True, "The button not clickable after 5 second"
