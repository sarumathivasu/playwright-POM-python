from playwright.sync_api import Playwright,Page
from utilities .test_data import USERNAME,PASSWORD
from pages.login__page import Loginpage

import pytest

@pytest.fixture

def login_to_application(page):
    login = Loginpage(page)
    login.url_redirection()
    login.login_methods(USERNAME,PASSWORD)
    return page
