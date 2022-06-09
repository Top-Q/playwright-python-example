from playwright.sync_api import Page, Locator

from infra.page.asbtract_component import AbsComponent


class Cell(AbsComponent):

    def __init__(self, page: Page, root: Locator):
        super().__init__(page, root)

    def get_value(self) -> str:
        return self._root.locator("span.inline-edit--display-field").inner_text()


class DeleteConfirmationDialogComp(AbsComponent):

    def __init__(self, page: Page, root: Locator):
        super().__init__(page, root)

    def click_on_confirm_btn(self):
        self._root.locator("button:has-text('Confirm')").click()


class RowContextMenu(AbsComponent):
    def __init__(self, page: Page, root: Locator):
        super().__init__(page, root)

    def click_on_delete_itm(self) ->DeleteConfirmationDialogComp:
        self._root.locator("[aria-label='Delete']").click()
        return DeleteConfirmationDialogComp(self._page, self._page.locator("id=wp_destroy_modal"))


class Row(AbsComponent):

    def __init__(self, page: Page, root: Locator):
        super().__init__(page, root)

    def get_cell(self, column_name: str) -> Cell:
        selector = f"//span[@data-field-name='{column_name.lower()}']/.."
        return Cell(self._page, self._root.locator(selector))

    def get_context_menu(self) -> RowContextMenu:
        locator = self._root.locator("i.icon-show-more-horizontal")
        locator.hover()
        locator.click()
        return RowContextMenu(self._page, self._page.locator("id=work-package-context-menu"))


class TableComponent(AbsComponent):

    def __init__(self, page: Page, root: Locator):
        super().__init__(page, root)

    def get_row(self, column_name: str, column_value: str) -> Row:
        selector = f"//span[@data-field-name='{column_name.lower()}' and text()='{column_value}']/../../.."
        row_root = self._root.locator(selector)
        if not row_root.is_visible():
            raise Exception("Row is not visible")
        return Row(self._page, row_root)

    def get_num_of_rows(self):
        return self._root.locator("tbody.results-tbody").count()
