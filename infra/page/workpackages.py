from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage
from infra.page.new_task import NewTaskPage
from infra.page.table_comp import TableComponent


class CreateMenuOptions(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._root: Locator = page.locator("div#types-context-menu")
        self._task_menu_itm: Locator = self._root.locator("a[aria-label='Task']")
        self._milestone_menu_itm: Locator = self._root.locator("a[aria-label='Milestone']")
        self._phase_menu_itm: Locator = self._root.locator("a[aria-label='Phase']")

    def goto(self):
        raise NotImplemented()

    def click_on_task_itm(self) -> NewTaskPage:
        self._task_menu_itm.click()
        return NewTaskPage(self._page)


class FilterPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._filter_by_text_tb: Locator = page.locator("id=filter-by-text-input")

    def goto(self):
        raise NotImplemented()

    def fill_filter_by_text_tb(self, text: str):
        with self._page.expect_response(url_or_predicate="**/queries/**") as response_info:
            self._filter_by_text_tb.fill(text)
        print(response_info.value.body())


class WorkPackagesPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._create_btn: Locator = page.locator("text=Create Include projects >> [aria-label='Create new work package']")
        self._filter_btn: Locator = page.locator("[aria-label='Activate Filter']")
        self.table = TableComponent(page, page.locator("table"))

    def goto(self, project_name: str) -> WorkPackagesPage:
        url = f"/projects/{project_name}/work_packages".lower().replace(" ", "-")
        self._page.goto(url, wait_until="networkidle")
        return self

    def click_on_create_btn(self) -> CreateMenuOptions:
        self._create_btn.click()
        return CreateMenuOptions(self._page)

    def click_on_filter_btn(self) -> FilterPage:
        self._filter_btn.click()
        return FilterPage(self._page)


