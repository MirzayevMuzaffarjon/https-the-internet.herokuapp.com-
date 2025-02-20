from playwright.sync_api import Page, expect
from Locators import Locators
from dotenv import load_dotenv
import os

class BasePage(Locators):
    def __init__(self, page : Page):
        super().__init__(page)
        self.page = page
        load_dotenv()

    @staticmethod
    def get_private_variable(key):
        return os.getenv(key)

    def open_home_page(self):
        self.page.goto(self.get_private_variable('base_url'))

    def wait(self, time):
        self.page.wait_for_timeout(time*1000)

    def check_home_page_opened_correctly(self):
        expect(self.home_page_welcome_text_locator).to_be_visible()
        expect(self.home_page_available_examples_text_locator).to_be_visible()