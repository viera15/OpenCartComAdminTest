import time

from selenium.webdriver.common.by import By

from pages.AdminPage import AdminPage
from pages.DashboardPage import DashboardPage
from tests.BaseTest import BaseTest



class TestDashboard(BaseTest):


    def test_logout_z_admin_prostredia(self):
        dashboard_page = self.login_spravne_udaje()
        dashboard_page.klik_na_logout()