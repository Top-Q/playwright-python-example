from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage
from infra.page.mainmenu import MainMenuPage


class OverviewPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._main_menu_btn: Locator = page.locator("id=main-menu-toggle")

    def goto(self, project_name: str) -> OverviewPage:
        self._page.goto(f"/projects/{project_name}".lower().replace(" ", "-"), wait_until="networkidle")
        return self

    def click_on_main_menu_btn(self) -> MainMenuPage:
        self._main_menu_btn.click()
        return MainMenuPage(self._page)

    def get_main_menu(self) -> MainMenuPage:
        return MainMenuPage(self._page)