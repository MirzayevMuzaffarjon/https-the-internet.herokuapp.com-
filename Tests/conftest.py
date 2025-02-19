import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=150)
        context = browser.new_context(viewport={"width": 1500, "height": 700})
        page = context.new_page()
        yield page
        context.close()
        browser.close()