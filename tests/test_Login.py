import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.AdminPage import AdminPage
from pages.DashboardPage import DashboardPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_spravne_udaje(self):
        admin_page = AdminPage(self.driver)
        admin_page.vpisat_admin_meno("demo")
        admin_page.vpisat_admin_heslo("demo")
        dashboard_page = admin_page.klik_na_login_tlacidlo()
        dashboard_page.zatvorenie_modalneho_okna()
        ocakavany_text = "Logout"
        assert dashboard_page.vratenie_textu_logout().__contains__(ocakavany_text)






