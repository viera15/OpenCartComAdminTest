import pytest

from pages.AdminPage import AdminPage
from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:


    def login_spravne_udaje(self):
        admin_page = AdminPage(self.driver)
        dashboard_page = admin_page.prihlasenie_admina("demo", "demo")
        dashboard_page.zatvorenie_modalneho_okna()
        return DashboardPage(self.driver)
