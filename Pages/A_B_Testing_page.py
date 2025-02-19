from playwright.sync_api import expect
from Pages.Base_page import BasePage

class ABTestingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def click_on_ab_testing_page_link(self):
        self.ab_testing_page_link.click()

    def check_ab_testing_page_opened_correctly(self):
        expect(self.ab_testing_page_heading_text_locator).to_be_visible()