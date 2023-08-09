from pages.widgets_page import AccordianPage


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
