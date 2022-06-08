import pytest
from playwright.sync_api import Page


@pytest.mark.skip(reason="Just a different selectors example")
def test_text_selectors(page: Page):
    #  Test Locators: default matching is case-insensitive and searches for a substring
    page.locator("text=Log in").click()

    # Fill the input by targeting the label.
    page.fill('text=Password', 'secret')

    # select elements that have some text somewhere inside,
    # possibly in a descendant element. Matching is case-insensitive and searches for a substring
    page.locator("button", has_text="Click me").click()


@pytest.mark.skip(reason="Just a different selectors example")
def test_css_xpath_selectors(page: Page):
    # css engine pierces open shadow DOM by default.
    # Playwright adds custom pseudo-classes like :visible, :text and more.
    page.locator("button").click()
    page.locator("button:visible").click()
    page.locator("button:has-text('Log in')").click()

    # Clicks a <button> that has either a "Log in" or "Sign in" text.
    page.locator('button:has-text("Log in"), button:has-text("Sign in")').click()

    # Fill an input to the right of "Username".
    page.locator("input:right-of(:text(\"Username\"))").fill("value")

    # Selector starting with // or .. is assumed to be an xpath selector. (doesn't pierce shadow roots  )
    page.locator("//html/body")


@pytest.mark.skip(reason="Just a different selectors example")
def test_chained_selectors(page: Page):
    # Chaining selectors
    page.locator("css=article >> css=.bar > .baz >> css=span[attr=value]")

    # Click first button
    page.locator("button >> nth=0").click()

    # By default, chained selectors resolve to an element queried by the last selector.
    # A selector can be prefixed with * to capture elements that are queried by an intermediate selector.
    page.locator("css=article >> text=Hello")
    page.locator("*css=article >> text=Hello")

    # only select elements that have a descendant matching another locator.
    page.locator("article", has=page.locator("button.subscribe"))


@pytest.mark.skip(reason="Just a different selectors example")
def test_special_selectors(page: Page):
    # React selectors - match by component
    page.locator("_react=BookItem")
    page.locator("_react=BookItem[author = 'Steven King']")

    # Vue selectors
    page.locator("_vue=book-item")

    # Click an element with data-test-id "submit" (id, data-testid, data-test-id, data-test)
    page.locator("data-test-id=submit").click()
