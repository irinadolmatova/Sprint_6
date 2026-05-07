import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class LogoPage(BasePage):
    
    @allure.step('Проверяем текущий URL')
    def check_open_page(self):
        return self.get_current_url()

    @allure.step('Клик по кнопке Заказать вверху страницы')
    def push_order_button(self):
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)
    
    @allure.step('Кликаем на логотип Самокат')
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Кликаем на логотип Яндекс')
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Переключаемся на новую вкладку и ждем URL')
    def switch_to_new_tab_and_wait_url(self, expected_url_part):
        self.switch_to_new_tab()
        self.wait_url_contains(expected_url_part)
