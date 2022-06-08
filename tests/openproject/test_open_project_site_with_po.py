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
        .click_on_main_menu_btn()\
        .click_on_work_package_itm()

    work_packages_page.click_on_create_btn()





