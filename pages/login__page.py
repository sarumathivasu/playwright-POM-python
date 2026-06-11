from playwright.sync_api import Playwright,Page

class Loginpage:
    def __init__(self,page:Page):
        self.page=page

        self.username=page.get_by_placeholder("Enter username")
        self.password=page.get_by_placeholder("Enter password")
        self.loginbutton=page.get_by_role('button', name='Login')


    def url_redirection(self):
        self.page.goto("https://qa.bloom365.com/app/")

    def login_methods(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginbutton.click()
