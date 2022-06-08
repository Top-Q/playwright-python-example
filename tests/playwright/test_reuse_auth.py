import pytest
from playwright.sync_api import Page, Browser


@pytest.fixture(scope="session", autouse=True)
def authenticate(browser: Browser) -> Browser:
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080/", wait_until="networkidle")
    page.locator("span:has-text('Sign in')").click()
    page.fill("text=Username", "admin")
    page.fill("text=Password", "adminadmin")

    with page.expect_response("**/login"):
        page.locator("input:has-text('Sign in')").click()

    context.storage_state(path=r"../../state.json")
    context.close()


@pytest.fixture(scope="function")
def auth_page(browser: Browser) -> Page:
    context = browser.new_context(storage_state=r"..\state.json")
    page = context.new_page()
    yield page
    page.close()


def test_use_storage_state_00(auth_page: Page):
    with auth_page.expect_navigation(url="http://localhost:8080/projects/selenium-project/"):
        auth_page.goto(url="http://localhost:8080/projects/selenium-project/")


def test_use_storage_state_01(auth_page: Page):
    with auth_page.expect_navigation(url="http://localhost:8080/projects/selenium-project/"):
        auth_page.goto(url="http://localhost:8080/projects/selenium-project/")


def test_use_storage_state_02(auth_page: Page):
    with auth_page.expect_navigation(url="http://localhost:8080/projects/selenium-project/"):
        auth_page.goto(url="http://localhost:8080/projects/selenium-project/")
