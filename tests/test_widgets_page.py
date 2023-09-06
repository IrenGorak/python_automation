from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgresBarPage, TabPage, \
    ToopTipPage, MenuPage, SelectMenuPage


class TestWidgetsPage:
    class TestAccordianPage:
        def test_accordian_page(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title_f, content_f = accordian_page.check_accordian('first')
            title_s, content_s = accordian_page.check_accordian('second')
            title_t, content_t = accordian_page.check_accordian('third')
            assert title_f == "What is Lorem Ipsum?", "The title is change or accordian no open"
            assert title_s == "Where does it come from?", "The title is change or accordian no open"
            assert title_t == "Why do we use it?", "The title is change or accordian no open"

    class TestAutoComplete:
        def test_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            color = auto_complete_page.fill_multi_input()
            color_result = auto_complete_page.check_color_multi()
            assert color == color_result, "Color does not equel color result"

        def test_remove_multi_value(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            auto_complete_page.fill_multi_input()
            count_value_before, count_value_after = auto_complete_page.remove_input()
            assert count_value_before != count_value_after, "The output equel input"

        def test_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            color = auto_complete_page.fill_single_input()
            color_result = auto_complete_page.check_single_color()
            assert color == color_result, "The output does not equel input"

    class TestDataPickerPage:

        def test_change_data(self, driver):
            data_picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date()
            assert value_date_before != value_date_after, "The date is the same"

        def test_change_data_and_time(self, driver):
            data_picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, "Date and time is not change"

    class TestSliderPage:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, "After value is the same as before"

        def test_progress_bar(self, driver):
            progress_bar = ProgresBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar.open()
            before, after = progress_bar.check_progress_bar()
            assert before != after, "The progress bar is not change"

    class TestTabs:
        def test_open_tabs(self, driver):
            tab_page = TabPage(driver, "https://demoqa.com/tabs")
            tab_page.open()
            what_button, what_content = tab_page.check_open_tab('what')
            origin_button, origin_content = tab_page.check_open_tab('origin')
            use_button, use_content = tab_page.check_open_tab('use')
            assert what_button == 'What' and what_content != 0, "The tab 'what' was not present or the the is missing"
            assert origin_button == 'Origin' and origin_content != 0, \
                "The tab 'origin' was not present or the the is missing"
            assert use_button == 'Use' and use_content != 0, "The tab 'use' was not present or the the is missing"

    class TestToolTips:
        def test_tool_tips(self, driver):
            tool_tips_page = ToopTipPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            button_text, field_text, link_text, number_text = tool_tips_page.check_tool_tips()
            assert button_text == "You hovered over the Button", "Hover missing or incorrect text"
            assert field_text == "You hovered over the text field", "Hover missing or incorrect text"
            assert link_text == "You hovered over the Contrary", "Hover missing or incorrect text"
            assert number_text == "You hovered over the 1.10.32", "Hover missing or incorrect text"

    class TestMenu:
        def test_open_menu(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            data = menu_page.check_menu()
            result = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                      'Sub Sub Item 2', 'Main Item 3']
            assert data == result, "Some tabs is not open or click"

    class TestSelectMenu:
        def test_check_select_menu(self, driver):
            select_menu = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            select_menu.open()
            select_menu.check_select_menu()
