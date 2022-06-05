from playwright.sync_api import Browser


def test_save_storage_state(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080/", wait_until="networkidle")
    page.locator("span:has-text('Sign in')").click()
    page.fill("text=Username", "admin")
    page.fill("text=Password", "adminadmin")

    with page.expect_response("**/login"):
        page.locator("input:has-text('Sign in')").click()

    context.storage_state(path=r"..\state.json")


def test_use_storage_state(browser: Browser):
    context = browser.new_context(storage_state=r"..\state.json")
    page = context.new_page()

    with page.expect_navigation(url="http://localhost:8080/projects/selenium-project/"):
        page.goto(url="http://localhost:8080/projects/selenium-project/")
