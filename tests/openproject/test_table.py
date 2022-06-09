from assertpy import assert_that
from playwright.sync_api import Page

from infra.page.workpackages import WorkPackagesPage


def test_create_and_delete_task(auth_page: Page):
    task_name = "Task xpqqvijrod"
    work_packages_page = WorkPackagesPage(auth_page)
    work_packages_page \
        .goto("Selenium project")
    row = work_packages_page.table.get_row("subject", task_name)
    cell = row.get_cell("subject")
    assert_that(cell.get_value()).is_equal_to(task_name)

    row\
        .get_context_menu()\
        .click_on_delete_itm()\
        .click_on_confirm_btn()