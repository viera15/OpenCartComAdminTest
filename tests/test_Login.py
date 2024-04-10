import pytest

from pages.AdminPage import AdminPage
from tests.BaseTest import BaseTest



class TestLogin(BaseTest):

    def test_login_spravne_udaje(self):
        admin_page = AdminPage(self.driver)
        dashboard_page = admin_page.prihlasenie_admina("demo", "demo")
        dashboard_page.zatvorenie_modalneho_okna()
        ocakavany_text = "Logout"
        assert dashboard_page.vratenie_textu_logout().__contains__(ocakavany_text)






