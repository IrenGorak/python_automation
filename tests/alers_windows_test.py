from pages.alerts_windows_page import WindowsPage, AlertsPage


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
