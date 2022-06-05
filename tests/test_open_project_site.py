import pytest
import string
import random
from playwright.sync_api import sync_playwright, expect


@pytest.fixture
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


trace = True
log_network = True
capture_video = False


@pytest.fixture()
def page(browser):
    if capture_video:
        context = browser.new_context(record_video_dir="playwright/videos/")
    else:
        context = browser.new_context()
    if trace:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    if log_network:
        page.on("request", lambda request: print(">>", request.method, request.url))
        page.on("response", lambda response: print("<<", response.status, response.url))

    yield page
    if trace:
        context.tracing.stop(path="../trace.zip")
    context.close()


def random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def test_create_and_delete_task(page):
    page.goto("http://localhost:8080/", wait_until="networkidle")
    page.locator("span:has-text('Sign in')").click()
    page.locator("input[name='username']").fill("admin")
    page.locator("input[name='password']").fill("adminadmin")

    with page.expect_response("**/login") as response_info:
        page.locator("input:has-text('Sign in')").click()
    print(f"{response_info.value.status_text}({response_info.value.status}) - {response_info.value.url}")

    expect(page).to_have_url("http://localhost:8080/")
    page.locator("#projects-menu i").click()

    with page.expect_navigation(url="http://localhost:8080/projects/selenium-project/"):
        page.locator("#ui-id-5 >> text=Selenium project").click()

    with page.expect_navigation(url="http://localhost:8080/projects/selenium-project/work_packages"):
        page.locator("#main-menu-work-packages >> text=Work packages").click()

    page.locator("text=Create Include projects >> [aria-label='Create new work package']").click()
    page.locator("div#types-context-menu a[aria-label='Task']").click()
    task_name = f"Task {random_string()}"
    page.locator("id=wp-new-inline-edit--field-subject").fill(task_name)
    with page.expect_navigation():
        page.locator("button:has-text('Save')").click()
    page.locator("[aria-label='Activate Filter']").click()
    page.locator("id=filter-by-text-input").fill(task_name)
    page.locator("a[title='Close form']").click()
    page.locator("button[title='Close details view'] i.icon-close.icon-no-color").click()
    page.locator("text='(1 - 1/1)'").wait_for()
    locator = page.locator("i.icon-show-more-horizontal")
    locator.hover()
    locator.click()
    page.locator("[aria-label='Delete']").click()

    page.locator("button:has-text('Confirm')").click()
    page.locator("text=Successfully deleted work packages.").wait_for()
    page.locator("text=No work packages to display.").wait_for()

    # ---------------------
