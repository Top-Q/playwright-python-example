import pytest
from playwright.sync_api import Page, sync_playwright


def test_matrix_site_without_pytest_plugin():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.matrix.co.il/")
        assert "לאתר הראשי הגלובלי" in page.inner_text("li.Matrix-global-site-btn")
        browser.close()


@pytest.mark.skip_browser("firefox")
def test_matrix_site_with_pytest_plugin(page: Page):
    page.goto("https://www.matrix.co.il/")
    assert "לאתר הראשי הגלובלי" in page.inner_text("li.Matrix-global-site-btn")
