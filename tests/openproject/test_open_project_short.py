import pytest
from playwright.sync_api import Page, Browser

from infra.page.overview import OverviewPage
from infra.page.welcome import WelcomePage
from infra.page.workpackages import WorkPackagesPage


@pytest.fixture(scope="session", autouse=True)
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
def auth_page(browser: Browser, pytestconfig) -> Page:
    context = browser.new_context(storage_state=r"../../state.json",base_url=pytestconfig.getoption('--base-url'))
    page = context.new_page()
    yield page
    page.close()


def test_create_and_delete_task_short(auth_page):
    overview_page = OverviewPage(auth_page)
    overview_page.goto("Selenium project")
    overview_page.click_on_main_menu_btn().click_on_work_package_itm()


def test_create_and_delete_task_short(auth_page):
    p = WorkPackagesPage(auth_page)
    p.goto("Selenium project")
    p.click_on_create_btn()
