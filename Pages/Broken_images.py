from playwright.sync_api import expect
from Pages.Base_page import BasePage

class BrokenImagesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open_broken_images_page(self):
        self.broken_images_page_locator.click()

    def check_broken_images_page_opened_correctly(self):
        expect(self.head_of_broken_images_page).to_be_visible()

    def check_images_are_broken(self):
        count = self.images.count()
        for i in range(count):
            image = self.images.nth(i)
            width = image.evaluate("img => img.naturalWidth")
            if width == 0:
                print(f" Buzilgan rasm topildi: {image.get_attribute('src')}")