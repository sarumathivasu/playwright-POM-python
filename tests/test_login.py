from pages.login__page import Loginpage
from utilities.test_data import USERNAME,PASSWORD


# ---------------- WITHOUT FIXTURE ----------------
# In every test we need to:
# 1. Create LoginPage object
# 2. Open application
# 3. Enter username and password
# 4. Login
#

def test_loginpage(page):
    login = Loginpage(page)
    login.url_redirection()
    login.login_methods(USERNAME,PASSWORD)

# ---------------- WITH FIXTURE ----------------
# login_to_application(conftest.py) fixture already performs:
# 1. Open application
# 2. Login with username and password
# 3. Return logged-in page
#
# So no need to repeat login steps in every test.

def test_case001(login_to_application):

    assert "dashboard" in login_to_application.url
