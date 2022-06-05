from playwright.sync_api import expect


def login(page, user: str, password: str):
    page.locator("span:has-text('Sign in')").click()
    # Fill input[name="username"]
    page.locator("input[name='username']").fill(user)
    # Fill input[name="password"]
    page.locator("input[name='password']").fill(password)
    # Click input:has-text("Sign in")
    with page.expect_response("**/login") as response_info:
        page.locator("input:has-text('Sign in')").click()
    print(response_info.value)
    expect(page).to_have_url("http://localhost:8080/")