from abc import ABC

from playwright.sync_api import Page


class AbsPage(ABC):

    def __init__(self, page: Page):
        self._page = page

    # def __getattribute__(self, attr_name: str):
    #     if not attr_name.startswith("_"):
    #         print(attr_name)
    #     return object.__getattribute__(self, attr_name)
