
from playwright.sync_api import Page, expect, Playwright


def test_google(page: Page):
    page.goto("http://www.google.com")
    page.get_by_role("combobox", name="חיפוש").fill("Cheese")
    locator = page.get_by_role("img", name="Google")
    locator.click()
    page.pause()
    page.get_by_role("button", name="חיפוש ב-Google").click()
    page.get_by_role("link", name="צ'יז בית הלל - אודות - מסעדה איטלקית בבית הלל https://cheeserestaurant.co.il").click()

