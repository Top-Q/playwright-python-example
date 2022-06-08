from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage
from infra.page.overview import OverviewPage


class OpenProjectPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._select_a_project_toggle: Locator = page.locator("#projects-menu i")

    def goto(self):
        self._page.goto("/", wait_until="networkidle")

    def click_on_select_a_project_toggle(self) -> OpenProjectPage:
        self._select_a_project_toggle.click()
        return self

    def click_on_project_name(self, project_name: str) -> OverviewPage:
        with self._page.expect_navigation(url=f"**/{project_name}/".replace(" ", "-").lower()):
            self._page.locator(f"#ui-id-5 >> text={project_name}").click()
        return OverviewPage(self._page)

    def do_select_project(self, project_name: str) -> OverviewPage:
        self.click_on_select_a_project_toggle()
        self.click_on_project_name(project_name)
        return OverviewPage(self._page)

