from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.AttributeGroupPage import AttributeGroupPage
from pages.AttributePage import AttributePage
from pages.BasePage import BasePage
from pages.CatalogPage import CatalogPage
from pages.FilterPage import FilterPage
from pages.HomeStorePage import HomeStorePage
from pages.ProductPage import ProductPage
from pages.ProfilePage import ProfilePage
from pages.SubscriptionPage import SubscriptionPage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        
    modal_window_xpath = "//div[@class='modal-dialog']"
    button_modal_window_xpath = "//button[@class='btn-close']"
    logout_option_xpath = "//header/div/ul/li[3]/a/span"
    logo_cesta_xpath = "//img[@title= 'OpenCart']"
    profil_dropdown_xpath = "//span[@class= 'd-none d-md-inline d-lg-inline']"
    list_profil_options_xpath = "//li[@id= 'header-profile']//a[@class= 'dropdown-item']"
    your_profile_option_link_text = "Your Profile"
    your_store_option_link_text = "Your Store"
    opencart_homepage_option_link_text = "OpenCart Homepage"
    documentation_option_link_text = "Documentation"
    navigation_menu_xpath = "//nav[@id= 'column-left']/ul/li"
    dashboard_nav_menu_option_xpath = "//li[@id= 'menu-dashboard']//a[contains(text(), 'Dashboard')]"
    dasboard_content_header_xpath = "//li[@class='breadcrumb-item']//a[contains(text(),'Dashboard')]"
    catalog_nav_menu_option_xpath = "//a[normalize-space()='Catalog']"
    #catalog_options_nav_menu_xpath = "//li[@id= 'menu-catalog']//a"
    categories_nav_menu_option_link_text = "Categories"
    products_nav_menu_option_xpath = "//a[normalize-space()='Products']"
    subscriptions_plans_nav_menu_option_xpath = "//a[normalize-space()='Subscription Plans']"
    filters_nav_menu_option_xpath = "//a[normalize-space()='Filters']"
    attributes_nav_menu_option_xpath = "//a[@class='parent collapsed'][normalize-space()='Attributes']"
    attributes_attributes_nav_menu_option_xpath = "//ul[@id='collapse-1-4']//a[contains(text(),'Attributes')]"
    attributes_attribute_groups_nav_menu_option_xpath = "//a[normalize-space()='Attribute Groups']"


#---------------modálne okno-----------------------------------------------------------------------------
    def cakanie_na_modalne_okno(self):
        wait = WebDriverWait(self.driver, 35)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.modal_window_xpath)))

    def klik_na_tlacidlo_modalneho_okna(self):
        #modalne_okno = self.driver.find_element(By.XPATH, "button_modal_window_xpath")
        #self.driver.execute_script("arguments[0].click();", modalne_okno)
        self.klik_na_element("button_modal_window_xpath", self.button_modal_window_xpath)
        
    def zatvorenie_modalneho_okna(self):
        self.cakanie_na_modalne_okno()
        return self.klik_na_tlacidlo_modalneho_okna()
#----------------------------------------------------------------------------------------------------------

    def vratenie_textu_logout(self):
        return self.ziskanie_textu_elementu("logout_option_xpath", self.logout_option_xpath)

    def klik_na_logout(self):
        self.klik_na_element("logout_option_xpath", self.logout_option_xpath)

    def zobrazovanie_loga(self):
        return self.kontrola_zobrazovania_elementu("logo_cesta_xpath", self.logo_cesta_xpath)

    # --------------------------------profil menu------------------------------------------------------------
    def vratenie_textu_dropdown_profilu(self):
        return self.ziskanie_textu_elementu("profil_dropdown_xpath", self.profil_dropdown_xpath)

    def klik_profil_dropdown_menu(self):
        self.klik_na_element("profil_dropdown_xpath", self.profil_dropdown_xpath)

    def klik_na_polozku_your_profile_profil_dropdown_menu(self):
        self.klik_profil_dropdown_menu()
        self.klik_na_element("your_profile_option_link_text", self.your_profile_option_link_text)
        return ProfilePage(self.driver)

    def klik_na_polozku_your_store_profil_dropdown_menu(self):
        self.klik_profil_dropdown_menu()
        self.klik_na_element("your_store_option_link_text", self.your_store_option_link_text)
        return HomeStorePage(self.driver)

    def klik_na_polozku_opencart_homepage_profil_dropdown_menu(self, nazov_title):
        self.klik_profil_dropdown_menu()
        self.klik_na_element("opencart_homepage_option_link_text",self.opencart_homepage_option_link_text)
        return self.prepnutie_do_okna_podla_title(nazov_title)

    def klik_na_položku_documentation_profil_dropdown_menu(self, nazov_title):
        self.klik_profil_dropdown_menu()
        self.klik_na_element("documentation_option_link_text", self.documentation_option_link_text)
        return self.prepnutie_do_okna_podla_title(nazov_title)

#----------------------navigation menu --------------------------------------------------------------------------------

#-----------------Dashboard--------------------------------------
    def klik_na_polozku_navigacneho_menu_dashboard(self):
        self.klik_na_element("dashboard_nav_menu_option_xpath", self.dashboard_nav_menu_option_xpath)

    def vratenie_textu_z_hlavicky_obsahovej_casti_dashboard(self):
        self.zatvorenie_modalneho_okna()
        return self.ziskanie_textu_elementu("dasboard_content_header_xpath",
                self.dasboard_content_header_xpath)

    def overenie_polozky_navigacneho_menu_dashboard(self):
        self.klik_na_polozku_navigacneho_menu_dashboard()
        return self.vratenie_textu_z_hlavicky_obsahovej_casti_dashboard()

#-----------------Catalog--------------------------------------------------

    def klik_na_polozku_navigacneho_menu_catalog(self):
        self.klik_na_element("catalog_nav_menu_option_xpath", self.catalog_nav_menu_option_xpath)

    #TODO overenie zoznamu položiek Catalog

#------------Catalog - Categories-------------------------------------------

    def klik_na_polozku_navigacneho_menu_catalog_categories(self):
        self.klik_na_polozku_navigacneho_menu_catalog()
        self.klik_na_element("categories_nav_menu_option_link_text", self.categories_nav_menu_option_link_text)
        return CatalogPage(self.driver)

#-------------Catalog - Products-----------------------------------------------------

    def klik_na_polozku_navigacneho_menu_catalog_products(self):
        self.klik_na_polozku_navigacneho_menu_catalog()
        self.klik_na_element("products_nav_menu_option_xpath", self.products_nav_menu_option_xpath)
        return ProductPage(self.driver)

#-----------Catalog - Subscriptions Plans----------------------------------------------

    def klik_na_polozku_navigacneho_menu_catalog_subscriptions_plans(self):
        self.klik_na_polozku_navigacneho_menu_catalog()
        self.klik_na_element("subscriptions_plans_nav_menu_option_xpath",
            self.subscriptions_plans_nav_menu_option_xpath)
        return SubscriptionPage(self.driver)

#------------Catalog - Filters---------------------------------------------------------

    def klik_na_polozku_navigacneho_menu_catalog_filters(self):
        self.klik_na_polozku_navigacneho_menu_catalog()
        self.klik_na_element("filters_nav_menu_option_xpath", self.filters_nav_menu_option_xpath)
        return FilterPage(self.driver)


#---------------Catalog - Attributes ------------------------------------------------------

    def klik_na_polozku_navigacneho_menu_catalog_attributtes(self):
        self.klik_na_polozku_navigacneho_menu_catalog()
        self.klik_na_element("attributes_nav_menu_option_xpath", self.attributes_nav_menu_option_xpath)

    #TODO overenie zoznamu položiek Attributes

    def klik_na_polozku_navigacneho_menu_attributes_attributes(self):
        self.klik_na_polozku_navigacneho_menu_catalog_attributtes()
        self.klik_na_element("attributes_attributes_nav_menu_option_xpath",
                self.attributes_attributes_nav_menu_option_xpath)
        return AttributePage(self.driver)

    def klik_na_polozku_navigacneho_menu_attributes_attribute_groups(self):
        self.klik_na_polozku_navigacneho_menu_catalog_attributtes()
        self.klik_na_element("attributes_attribute_groups_nav_menu_option_xpath",
                self.attributes_attribute_groups_nav_menu_option_xpath)
        return AttributeGroupPage(self.driver)








