from playwright.sync_api import Page

from infra.po.abstract_page import AbsPage


class OpenProjectPage(AbsPage):

    def __init__(self, page: Page):
        super().__init__(page)