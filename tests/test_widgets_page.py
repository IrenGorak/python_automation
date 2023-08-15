import time
from pages.widgets_page import AccordianPage, AutoCompletePage


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

