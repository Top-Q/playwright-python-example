import pytest
from playwright.sync_api import Page, sync_playwright


def test_google_site_without_pytest_plugin():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com/")
        page.locator("[name='q']").fill("Matrix Top-Q")
        with page.expect_navigation():
            page.locator("text=חיפוש ב-Google >> nth=1").click()
        assert "מטריקס בדיקות ואוטומציה" in page.locator("h3 >> nth=1").inner_text()
        browser.close()


@pytest.mark.skip_browser("firefox")
def test_google_site_with_pytest_plugin(page: Page):
    page.goto("https://www.google.com/")
    page.locator("[name='q']").fill("Matrix Top-Q")
    with page.expect_navigation():
        page.locator("text=חיפוש ב-Google >> nth=1").click()
    assert "מטריקס בדיקות ואוטומציה" in page.locator("h3 >> nth=1").inner_text()
