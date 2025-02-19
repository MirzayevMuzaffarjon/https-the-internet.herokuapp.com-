from playwright.sync_api import expect

from Pages.Base_page import BasePage

class AddRemoveElementPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open_add_remove_page(self):
        self.add_remove_element_page_locator.click()

    def check_add_remove_page_opened_correctly(self):
        expect(self.head_of_add_remove_page).to_be_visible()
        expect(self.add_remove_page_add_element_button).to_be_visible()
        expect(self.add_remove_page_delete_button).not_to_be_visible()

    def click_add_element(self):
        self.add_remove_page_add_element_button.click()

    def check_element_added_successfully(self):
        expect(self.add_remove_page_delete_button).to_be_visible()

    def click_delete_button(self):
        self.add_remove_page_delete_button.click()

    def check_element_deleted_successfully(self):
        expect(self.add_remove_page_delete_button).not_to_be_visible()


