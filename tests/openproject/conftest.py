import pytest
from playwright.sync_api import Browser, Page

from infra.page.welcome import WelcomePage


@pytest.fixture(scope="session")
def authenticate(browser: Browser, pytestconfig) -> Browser:
    base_url = pytestconfig.getoption('--base-url')
    if base_url:
        context = browser.new_context(base_url=base_url)
    else:
        context = browser.new_context()
    welcome_page = WelcomePage(context.new_page())
    welcome_page.goto() \
        .click_on_sign_in_toggle() \
        .fill_username_tb(username="admin") \
        .fill_password_tb("adminadmin") \
        .click_on_sign_in_btn_and_goto_open_project_page()
    context.storage_state(path=r"../../state.json")
    context.close()


@pytest.fixture(scope="function")
def auth_page(authenticate, browser: Browser, pytestconfig) -> Page:
    context = browser.new_context(storage_state=r"../../state.json",base_url=pytestconfig.getoption('--base-url'))
    page = context.new_page()
    yield page
    page.close()