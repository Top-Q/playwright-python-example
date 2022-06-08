from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.po.abstract_page import AbsPage
from infra.po.open_project_page import OpenProjectPage
from infra.print_decorator import step


class WelcomePage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._sign_in_toggle: Locator = page.locator("span:has-text('Sign in')")
        self._username_label: Locator = page.locator("text=Username")
        self._password_label: Locator = page.locator("label[title='Password']")
        self._sign_in_btn: Locator = page.locator("input:has-text('Sign in')")

    @step
    def goto(self) -> WelcomePage:
        self._page.goto("/", wait_until="networkidle")
        return self

    @step
    def click_on_sign_in_toggle(self) -> WelcomePage:
        self._sign_in_toggle.click()
        return self

    @step
    def fill_username_tb(self, username) -> WelcomePage:
        self._username_label.fill(username)
        return self

    @step
    def fill_password_tb(self, password) -> WelcomePage:
        self._password_label.fill(password)
        return self

    @step
    def click_on_sign_in_btn_and_goto_open_project_page(self) -> OpenProjectPage:
        with self._page.expect_response("**/login"):
            self._sign_in_btn.click()
        return OpenProjectPage(self._page)
