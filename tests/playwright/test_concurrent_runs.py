from playwright.sync_api import Page, expect

# This should be executed with the xdist plugin


def repeated_logic(page: Page):
    page.goto("/", wait_until="networkidle")
    page.locator("span:has-text('Sign in')").click()
    page.fill("text=Username", "admin")
    page.fill("text=Password", "adminadmin")

    with page.expect_response("**/login") as response_info:
        page.locator("input:has-text('Sign in')").click()
    print(f"{response_info.value.status_text}({response_info.value.status}) - {response_info.value.url}")
    expect(page).to_have_url("http://localhost:8080/")
    page.locator("#projects-menu i").click()

    with page.expect_navigation(url="http://localhost:8080/projects/selenium-project/"):
        page.locator("#ui-id-5 >> text=Selenium project").click()

    with page.expect_navigation(url="http://localhost:8080/projects/selenium-project/work_packages"):
        page.locator("#main-menu-work-packages >> text=Work packages").click()


def test_00(page: Page):
    repeated_logic(page)


def test_01(page: Page):
    repeated_logic(page)


def test_02(page: Page):
    repeated_logic(page)


def test_03(page: Page):
    repeated_logic(page)

