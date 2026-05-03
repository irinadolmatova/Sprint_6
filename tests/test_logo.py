import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.logo_page import LogoPage
from URL import *

class TestLogo:
    @allure.title('Проверка перехода на главную при клике на логотип Самоката')
    def test_click_logo_scooter_open_main_page(self, driver):
        page = LogoPage(driver)
        page.push_order_button()
        page.click_logo_scooter()
        assert page.check_open_page() == MAIN_URL

    @allure.title('Проверка перехода на Дзен при клике на логотип Яндекса')
    def test_click_logo_yandex_open_dzen(self, driver):
        page = LogoPage(driver)
        page.click_logo_yandex()
        page.switch_to_new_tab()
        page.wait_url_contains("dzen.ru")
        assert "dzen.ru" in page.check_open_page()