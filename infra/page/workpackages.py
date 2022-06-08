from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage


class WorkPackagesPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._create_btn: Locator = page.locator("text=Create Include projects >> [aria-label='Create new work package']")

    def goto(self, project_name: str) -> WorkPackagesPage:
        url = f"/projects/{project_name}/work_packages".lower().replace(" ", "-")
        self._page.goto(url, wait_until="networkidle")
        return self

    def click_on_create_btn(self):
        self._create_btn.click()