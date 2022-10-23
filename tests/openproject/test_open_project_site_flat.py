import string
import random
from playwright.sync_api import expect, Page


def test_create_and_delete_task(page: Page):
    page.goto("/", wait_until="networkidle")

    page.locator("span:has-text('Sign in')").click()
    page.fill("text=Username", "admin")
    page.fill("text=Password", "adminadmin")

    with page.expect_response("**/login") as response_info:
        page.locator("input:has-text('Sign in')").click()
    print(f"{response_info.value.status_text}({response_info.value.status}) - {response_info.value.url}")
    expect(page).to_have_url("http://localhost:8080/")
    page.wait_for_load_state(event="networkidle")

    page.locator("#projects-menu i").click()

    with page.expect_navigation(url="http://localhost:8080/projects/selenium-project/"):
        page.locator("#ui-id-5 >> text=Selenium project").click()
    page.pause()
    with page.expect_navigation(url="http://localhost:8080/projects/selenium-project/work_packages"):
        page.locator("#main-menu-work-packages >> text=Work packages").click()

    page.locator("text=Create Include projects >> [aria-label='Create new work package']").click()
    page.locator("div#types-context-menu a[aria-label='Task']").click()
    task_name = f"Task {''.join(random.choice(string.ascii_lowercase) for i in range(10))}"
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
