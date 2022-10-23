from playwright.sync_api import Page


def test_events(page: Page):

    def print_event(something):
        print(f"Event: {something}")

    page.goto("https://www.google.com/")
    page.on(event="click", f=print_event)
    page.locator("[name='q']").fill("Matrix Top-Q")
    with page.expect_navigation():
        btn_locator = page.locator("text=חיפוש ב-Google >> nth=1")
        btn_locator.click()

