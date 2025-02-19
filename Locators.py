from playwright.sync_api import Page

class Locators:
    def __init__(self, page:Page):
        self.page = page
        self.ab_testing_page_link = page.get_by_role("link", name="A/B Testing")
        self.home_page_welcome_text_locator = self.page.get_by_role("heading", name="Welcome to the-internet")
        self.home_page_available_examples_text_locator = self.page.get_by_role("heading", name="Available Examples")
        self.ab_testing_page_heading_text_locator = self.page.locator('//div[@class="example"]/h3')
        self.add_remove_element_page_locator = self.page.get_by_role("link", name="Add/Remove Elements")
        self.head_of_add_remove_page = self.page.get_by_role("heading", name="Add/Remove Elements")
        self.add_remove_page_add_element_button = self.page.get_by_role("button", name="Add Element")
        self.add_remove_page_delete_button = self.page.get_by_role("button", name="Delete")