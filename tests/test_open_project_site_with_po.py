import pytest
from playwright.sync_api import Page

from infra.po.welcome_page import WelcomePage

def test_create_and_delete_task(page: Page):
    welcome_page = WelcomePage(page)
    open_project_page = welcome_page\
        .goto()\
        .click_on_sign_in_toggle()\
        .fill_username_tb(username="admin")\
        .fill_password_tb("adminadmin")\
        .click_on_sign_in_btn_and_goto_open_project_page()
