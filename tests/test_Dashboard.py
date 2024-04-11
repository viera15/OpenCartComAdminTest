from selenium.webdriver.common.by import By

from pages.AdminPage import AdminPage
from tests.BaseTest import BaseTest



class TestDashboard(BaseTest):


    def test_logout_z_admin_prostredia(self):
        admin_page = AdminPage(self.driver)
        dashboard_page = admin_page.prihlasenie_admina("demo", "demo")
        dashboard_page.zatvorenie_modalneho_okna()
        dashboard_page.klik_na_logout()