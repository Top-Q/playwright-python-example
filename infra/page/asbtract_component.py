from abc import ABC

from difido.report_manager import Report
from playwright.sync_api import Page, Locator


class AbsComponent(ABC):

    def __init__(self, page: Page, root: Locator):
        self._page = page
        self._root = root
        self._report = Report()

    def __getattribute__(self, attr_name: str):
        if not attr_name.startswith("_"):
            message = "\t" + attr_name.replace('_', ' ').capitalize()
            self._report.that(message)
        return object.__getattribute__(self, attr_name)
