from Pages.A_B_Testing_page import ABTestingPage
from Pages.Add_Remove_element_page import AddRemoveElementPage
from Pages.Broken_images import BrokenImagesPage


def test_ab_testing_page(page):
    user = ABTestingPage(page)
    user.open_home_page()
    user.check_home_page_opened_correctly()
    user.click_on_ab_testing_page_link()
    user.check_ab_testing_page_opened_correctly()

def test_add_remove_page(page):
    user = AddRemoveElementPage(page)
    user.open_home_page()
    user.check_home_page_opened_correctly()
    user.open_add_remove_page()
    user.check_add_remove_page_opened_correctly()
    user.click_add_element()
    user.check_element_added_successfully()
    user.click_delete_button()
    user.check_element_deleted_successfully()

def test_broken_images_page(page):
    user = BrokenImagesPage(page)
    user.open_home_page()
    user.check_home_page_opened_correctly()
    user.open_broken_images_page()
    user.check_broken_images_page_opened_correctly()
    user.wait(1)
    user.check_images_are_broken()