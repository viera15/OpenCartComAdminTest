import pytest

from pages.AdminPage import AdminPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_spravne_udaje(self):
        admin_page = AdminPage(self.driver)
        dashboard_page = admin_page.prihlasenie_admina("demo", "demo")
        dashboard_page.zatvorenie_modalneho_okna()
        ocakavany_text = "Logout"
        assert dashboard_page.vratenie_textu_logout().__contains__(ocakavany_text)






