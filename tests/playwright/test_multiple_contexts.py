from playwright.sync_api import Browser


def test_multiple_contexts(browser: Browser):
    user_context = browser.new_context()
    user_page = user_context.new_page()
    user_page.goto("http://localhost:8080")
    user_page.locator("span:has-text('Sign in')").click()
    user_page.locator("input[name='username']").fill("user")
    user_page.locator("input[name='password']").fill("useruseruser")
    with user_page.expect_navigation():
        user_page.locator("input:has-text('Sign in')").click()

    admin_context = browser.new_context()
    admin_page = admin_context.new_page()
    admin_page.goto("http://localhost:8080")
    admin_page.locator("span:has-text('Sign in')").click()
    admin_page.locator("input[name='username']").fill("admin")
    admin_page.locator("input[name='password']").fill("adminadmin")
    with admin_page.expect_navigation():
        admin_page.locator("input:has-text('Sign in')").click()

