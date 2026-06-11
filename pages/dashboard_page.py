from playwright.sync_api import Playwright,Page

class Dashboardpage:
    def __init__(self,page:Page):
        self.page=page
        
        self.dashboard_text=page.get_by_text("Welcome back,")
        self.dashboard_text1=page.get_by_text("Completed Applications")
        self.dashboard_text2=page.get_by_text("Applications In Progress ")


    def is_dashboard_loaded(self):
        return (
            self.dashboard_text.is_visible() and

            self.dashboard_text1.is_visible() and

            self.dashboard_text2.is_visible() 
            )
    
    def wait_dashboard_fully_loaded(self):
        self.page.wait_for_load_state("networkidle")