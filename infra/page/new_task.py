from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage


class NewTaskPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._task_name_tb: Locator = page.locator("id=wp-new-inline-edit--field-subject")
        self._save_btn: Locator = page.locator("button:has-text('Save')")

    def goto(self, project_name: str) -> NewTaskPage:
        # http: // localhost: 8080 / projects / selenium - project / work_packages / create_new?type = 1
        url = f"/projects/{project_name}/work_packages/create_new?type=1".lower().replace(" ", "-")
        self._page.goto(url, wait_until="networkidle")
        return self

    def fill_task_name_tb(self, task_name: str) -> NewTaskPage:
        self._task_name_tb.fill(task_name)
        return self

    def click_on_save_btn(self):
        self._save_btn.click()
