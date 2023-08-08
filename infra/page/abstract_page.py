import os.path
import re
import tempfile
from abc import ABC, abstractmethod

from playwright.sync_api import Page

from infra.page.asbtract_component import AbsComponent


class AbsPage(AbsComponent):

    def __init__(self, page: Page):
        super().__init__(page, page)
        page_name = re.sub(r"(\w)([A-Z])", r"\1 \2", type(self).__name__)
        screenshot_file = os.path.join(tempfile.gettempdir(), f'{page_name}-screenshot.png')
        page.screenshot(path=screenshot_file)
        self._report.img(description=page_name, img_path=screenshot_file)

    @abstractmethod
    def goto(self):
        pass

