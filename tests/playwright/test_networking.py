from playwright.sync_api import Page


def test_mock_response(page):
    page.route("**/api/test", lambda route: route.fulfill(status=200, body="<h1>Great Success</h1>"))
    page.goto("https://localhost:8080/api/test")
    assert "Great Success" in page.inner_text("h1")
    page.pause()


def test_http_auth(browser):
    context = browser.new_context(
        http_credentials={"username": "admin", "password": "adminadmin"}
    )
    page = context.new_page()
    page.goto("http://localhost:8080/projects/selenium-project/")


def test_log_network(page: Page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto("https://www.matrix.co.il/")
    assert "לאתר הראשי הגלובלי" in page.inner_text("li.Matrix-global-site-btn")

