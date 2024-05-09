import time

from selenium.webdriver.common.by import By

from pages.AdminPage import AdminPage
from pages.CatalogPage import CatalogPage
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

    def test_kliknutie_na_your_profil_link(self):
        dashboard_page = self.login_spravne_udaje()
        profile_page = dashboard_page.klik_na_polozku_your_profile_profil_dropdown_menu()
        ocakavany_nazov_card_header = "Edit Your Profile"
        assert profile_page.vratenie_textu_card_header().__contains__(ocakavany_nazov_card_header)

    def test_kliknutie_na_your_store_profil_link(self):
        dashboard_page = self.login_spravne_udaje()
        home_store_page = dashboard_page.klik_na_polozku_your_store_profil_dropdown_menu()
        ocakavany_nazov_url = "https://demo.opencart.com/"
        assert home_store_page.vratenie_url_stranky_your_store().__contains__(ocakavany_nazov_url)
    def test_kliknutie_na_opencart_homepage_profil_link(self):
        dashboard_page = self.login_spravne_udaje()
        ocakavany_title_page = "OpenCart - Open Source Shopping Cart Solution"
        assert dashboard_page.klik_na_polozku_opencart_homepage_profil_dropdown_menu(ocakavany_title_page)

    def test_kliknutie_na_documentation_profil_link(self):
        dashboard_page = self.login_spravne_udaje()
        ocakavany_title_page_text = "OpenCart Documentation"
        assert dashboard_page.klik_na_položku_documentation_profil_dropdown_menu(ocakavany_title_page_text)

    #TODO občas pozrieť, či stránka existuje
    def test_kliknutie_support_forum_profil_link(self):
        # stránka forum.opencart.com asi neexistuje
        pass

    def test_logout_z_admin_prostredia(self):
        dashboard_page = self.login_spravne_udaje()
        dashboard_page.klik_na_logout()

#---------------------NAV-------------------------------------------------------------------

    def test_kliknutie_na_dashboard_navigation_link(self):
        dashboard_page = self.login_spravne_udaje()
        ocakavany_nadpis_dashboard = "Dashboard"
        assert dashboard_page.overenie_polozky_navigacneho_menu_dashboard().__eq__(ocakavany_nadpis_dashboard)

    #TODO porovnanie zoznamu položiek Catalog s očakávaným zoznamom položiek
    def test_kliknutie_catalog_navigation_link(self):
        pass

    def test_kliknutie_catalog_categories_navigation_link(self):
        dashboard_page = self.login_spravne_udaje()
        catalog_page = dashboard_page.klik_na_polozku_navigacneho_menu_categories()
        ocakavany_nadpis_categories = "Categories"
        assert catalog_page.vratenie_textu_z_hlavicky_obsahovej_casti_categories().__eq__(ocakavany_nadpis_categories)

    def test_kliknutie_catalog_products_navigation_link(self):
        dashboard_page = self.login_spravne_udaje()
        product_page = dashboard_page.klik_na_polozku_navigacneho_menu_products()
        ocakavany_nadpis_products = "Products"
        assert product_page.vratenie_textu_z_hlavicky_obsahovej_casti_products().__eq__(ocakavany_nadpis_products)

    def test_kliknutie_catalog_subscription_plans_navigation_link(self):
        dashboard_page = self.login_spravne_udaje()
        subscription_page = dashboard_page.klik_na_polozku_navigacneho_menu_subscriptions_plans()
        ocakavany_nadpis_subscription = "Subscription Plans"
        assert subscription_page.vratenie_textu_z_hlavicky_obsahovej_casti_subscription_plan().__eq__(
            ocakavany_nadpis_subscription)







#--------------------CONTENT---------------------------------------------------------------


#--------------------FOOTER-----------------------------------------------------------------
