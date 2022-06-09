import random
import string

from assertpy import assert_that
from playwright.sync_api import Page
from infra.page.welcome import WelcomePage


def test_create_and_delete_task(page: Page):
    welcome_page = WelcomePage(page)
    open_project_page = welcome_page\
        .goto()\
        .click_on_sign_in_toggle()\
        .fill_username_tb(username="admin")\
        .fill_password_tb("adminadmin")\
        .click_on_sign_in_btn_and_goto_open_project_page()

    overview_page = open_project_page.do_select_project("Selenium project")
    work_packages_page = overview_page\
        .get_main_menu()\
        .click_on_work_package_itm()

    new_task_page = work_packages_page\
        .click_on_create_btn()\
        .click_on_task_itm()

    task_name = f"Task {''.join(random.choice(string.ascii_lowercase) for i in range(10))}"

    new_task_page\
        .fill_task_name_tb(task_name)\
        .click_on_save_btn()

    work_packages_page\
        .goto("Selenium project")\
        .click_on_filter_btn()\
        .fill_filter_by_text_tb(task_name)

    results = work_packages_page.get_num_of_results()
    assert_that(results).is_equal_to(1)






