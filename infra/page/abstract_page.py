import re
from abc import ABC, abstractmethod

from playwright.sync_api import Page

from infra.page.asbtract_component import AbsComponent


class AbsPage(AbsComponent):

    def __init__(self, page: Page):
        super().__init__(page, page)
        print(re.sub(r"(\w)([A-Z])", r"\1 \2", type(self).__name__))

    @abstractmethod
    def goto(self):
        pass

