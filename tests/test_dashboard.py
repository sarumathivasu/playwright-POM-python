from pages.login__page import Loginpage
from pages.dashboard_page import Dashboardpage
from utilities.test_data import USERNAME,PASSWORD

# ==================================================
# WITHOUT FIXTURE
# ==================================================
#
# Every test must:
# 1. Create LoginPage object
# 2. Open application URL
# 3. Login with username and password
# 4. Perform validation
#
# Drawback:
# Login code is repeated in every test.

def test_Verify_Dashboard_Access_Case001(page):
    login=Loginpage(page)
    dashboard=Dashboardpage(page)
    login.url_redirection()
    login.login_methods(USERNAME,PASSWORD)
    assert "dashboard" in page.url

def test_Verify_Dashboard_Loaded_Case002(page):
    login=Loginpage(page)
    dashboard=Dashboardpage(page)
    login.url_redirection()
    login.login_methods(USERNAME,PASSWORD)

    dashboard.wait_dashboard_fully_loaded()
    assert dashboard.is_dashboard_loaded()

# ==================================================
# WITH FIXTURE
# ==================================================
#
# login_to_application fixture is created in conftest.py
#
# The fixture automatically:
# 1. Opens application
# 2. Enters username
# 3. Enters password
# 4. Clicks Login
# 5. Returns logged-in page
#
# Advantage:
# No need to repeat login code in every test.
#

def test_withfixtures(login_to_application):
    assert "dashboard" in login_to_application.url

def test_case2_withfixtures(login_to_application):
    dashboard=Dashboardpage(login_to_application)
    dashboard.wait_dashboard_fully_loaded()
    assert dashboard.is_dashboard_loaded() 


