from pages.alerts_windows_page import WindowsPage, AlertsPage, FramePage, NestedFramePage


class TestAlertsWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_window = WindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window.open()
            text_result = browser_window.check_open_new_tab()
            assert text_result == "This is a sample page", 'The new tab wasn not openn or the text in incorrect'

        def test_new_window(self, driver):
            browser_window = WindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window.open()
            text_result = browser_window.check_open_new_window()
            assert text_result == "This is a sample page", 'The new tab wasn not openn or the text in incorrect'

    class TestAlertsPage:
        def test_alert_page(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == "You clicked a button", "The button is not clicked"

        def test_alert_5_seconds(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_alert_5_seconds()
            assert alert_text == "This alert appeared after 5 seconds", "The alert is not clikable"

        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == "You selected Ok" or "You selected Cancel", "The alert is not clickable"

        def test_promt_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text, alert_text = alerts_page.check_promt_alert()
            assert alert_text == f"You entered {text}", "The text is not in alert form"

    class TestFramePage:
        def test_frame_page(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_1 = frame_page.check_frames('frame1')
            result_2 = frame_page.check_frames('frame2')
            assert result_1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            nested_frame = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            nested_frame.open()
            parent_text, child_text = nested_frame.check_nested_frames()
            assert parent_text == "Parent frame", "The frame does not exist or the text is changed"
            assert child_text == "Child Iframe", 'The frame does not exist or the thext is changed'
