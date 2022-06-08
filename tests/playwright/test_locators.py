from playwright.sync_api import Page


def test_locators(page: Page):



    # Every time locator is
    # used for some action, up-to-date DOM element is located in the page.
    # So in the snippet below, underlying DOM element is going to be located twice, prior to every action.
    # This means that if the DOM changes in between the calls due to re-render,
    # the new element corresponding to the locator will be used.
    locator = page.locator("text=Submit")
    locator.hover()
    locator.click()

    # Throws if there are several buttons in DOM:
    page.locator('button').click()

    # Works because we explicitly tell locator to pick the first element:
    page.locator('button').first.click()

