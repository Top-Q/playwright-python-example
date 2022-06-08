
from playwright.sync_api import Playwright, APIRequestContext
from requests.auth import HTTPBasicAuth
import requests

token = "638029b55b4ebf01ab3e473ac7cf172f02d4f8939a88a845d7e2e308cca61e32"


def test_get_project_using_requests():
    url = f"http://localhost:8080/api/v3/projects/4"
    basic_auth = HTTPBasicAuth('apikey', f'{token}')
    response = requests.get(f"{url}", auth=basic_auth)
    print(response.json())


def test_get_project_using_playwright(playwright: Playwright):
    headers = {
        "apikey": f"{token}"
    }
    api_context = playwright.request.new_context(
        base_url="http://localhost:8080", extra_http_headers=headers
    )

    response = api_context.get("/api/v3/projects/2")
    print(response.json())
    api_context.dispose()
    