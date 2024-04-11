from selenium.webdriver.common.by import By

from pages.AdminPage import AdminPage
from tests.BaseTest import BaseTest



class TestLogin(BaseTest):

    def test_login_spravne_udaje(self):
        dashboard_page = self.login_spravne_udaje()
        ocakavany_text = "Logout"
        assert dashboard_page.vratenie_textu_logout().__contains__(ocakavany_text)

    def test_login_nespravne_udaje(self):
        admin_page = AdminPage(self.driver)
        admin_page.prihlasenie_admina("abcd", "efgh")
        ocakavane_upozornenie = "No match for Username and/or Password."
        assert admin_page.ziskanie_textu_upozornenia().__contains__(ocakavane_upozornenie)
        
    def test_login_nevyplnene_udaje(self):
        admin_page = AdminPage(self.driver)
        admin_page.prihlasenie_admina("", "")
        ocakavane_upozornenie = "No match for Username and/or Password."
        assert admin_page.ziskanie_textu_upozornenia().__contains__(ocakavane_upozornenie)

    def test_overenie_title_admin_stranky(self):
        ocakavany_title = "Administration"
        assert self.driver.title.__eq__(ocakavany_title)


