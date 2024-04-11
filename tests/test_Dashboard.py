import time

from selenium.webdriver.common.by import By

from pages.AdminPage import AdminPage
from pages.DashboardPage import DashboardPage
from tests.BaseTest import BaseTest



class TestDashboard(BaseTest):

#--------------------HEAD------------------------------------------------------------------

    def test_overenie_title_dashboard_stranky(self):
        self.login_spravne_udaje()
        ocakavany_title = "Dashboard"
        assert self.driver.title.__eq__(ocakavany_title)

#---------------------HEADER----------------------------------------------------------------

    def test_overenie_loga(self):
        dashboard_page = self.login_spravne_udaje()
        assert dashboard_page.zobrazovanie_loga()

    def test_overenie_textu_dropdown_menu_profilu(self):
        dashboard_page = self.login_spravne_udaje()
        ocakavany_text_dropdown_profilu = "demo demo"
        assert dashboard_page.vratenie_textu_dropdown_profilu().__contains__(ocakavany_text_dropdown_profilu)





    def test_logout_z_admin_prostredia(self):
        dashboard_page = self.login_spravne_udaje()
        dashboard_page.klik_na_logout()

#---------------------NAV-------------------------------------------------------------------


#--------------------FOOTER-----------------------------------------------------------------
