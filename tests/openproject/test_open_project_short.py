import random
import string

from assertpy import assert_that

from infra.page.new_task import NewTaskPage
from infra.page.overview import OverviewPage
from infra.page.workpackages import WorkPackagesPage


def test_goto_overview_page(auth_page):
    overview_page = OverviewPage(auth_page)
    overview_page.goto("Selenium project")
    overview_page.click_on_main_menu_btn().click_on_work_package_itm()


def test_goto_work_packages_page(auth_page):
    work_packages_page = WorkPackagesPage(auth_page)
    work_packages_page.goto("Selenium project")
    work_packages_page.click_on_create_btn()


def test_create_task(auth_page):
    new_task_page = NewTaskPage(auth_page)
    task_name = f"Task {''.join(random.choice(string.ascii_lowercase) for _ in range(10))}"
    new_task_page\
        .goto("Selenium project")\
        .fill_task_name_tb(task_name)\
        .click_on_save_btn()

    work_packages_page = WorkPackagesPage(auth_page)
    work_packages_page\
        .goto("Selenium project") \
        .click_on_filter_btn() \
        .fill_filter_by_text_tb(task_name)

    results = work_packages_page.table.get_num_of_rows()
    assert_that(results).is_equal_to(1)

    work_packages_page.table\
        .get_row("subject", task_name)\
        .get_context_menu()\
        .click_on_delete_itm()\
        .click_on_confirm_btn()


