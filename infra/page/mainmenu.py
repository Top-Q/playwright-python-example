from __future__ import annotations
from playwright.sync_api import Page, Locator

from infra.page.abstract_page import AbsPage
from infra.page.workpackages import WorkPackagesPage


class MainMenuPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._work_packages_itm: Locator = page.locator("#main-menu-work-packages >> text=Work packages")

    def goto(self) -> MainMenuPage:
        raise NotImplemented()

    def click_on_work_package_itm(self) -> WorkPackagesPage:
        self._work_packages_itm.click()
        return WorkPackagesPage(self._page)
