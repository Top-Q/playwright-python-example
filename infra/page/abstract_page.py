import re
from abc import ABC, abstractmethod

from playwright.sync_api import Page


class AbsPage(ABC):

    def __init__(self, page: Page):
        self._page = page
        print(re.sub(r"(\w)([A-Z])", r"\1 \2", type(self).__name__))

    @abstractmethod
    def goto(self):
        pass

    def __getattribute__(self, attr_name: str):
        if not attr_name.startswith("_"):
            print("\t" + attr_name.replace('_', ' ').capitalize())
        return object.__getattribute__(self, attr_name)
