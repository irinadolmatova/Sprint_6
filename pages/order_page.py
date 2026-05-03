import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Проверка текущего URL')
    def check_open_page(self):
        return self.get_current_url()
    
    @allure.step('Клик по кнопке Заказать внизу страницы')
    def push_order_button(self, locator_order_button):
        if locator_order_button == OrderPageLocators.FOOTER_ORDER_BUTTON:
            self.scroll_to_element(locator_order_button)
        self.click_element(locator_order_button)

    @allure.step('Заполнение поля Имя')
    def filling_name_field(self, name):
        self.set_text(OrderPageLocators.NAME, name)
    
    @allure.step('Заполнение поля Фамилия')
    def filling_surname_field(self, surname):
        self.set_text(OrderPageLocators.SURNAME, surname)

    @allure.step('Заполнение поля Адрес')
    def filling_adress_field(self, address):
        self.set_text(OrderPageLocators.ADRESS, address)

    @allure.step('Заполнение поля Станция метро')
    def filling_metro_field(self):
        element = self.find_element(OrderPageLocators.METRO)
        element.send_keys('Пушкинская')
        element.send_keys(Keys.DOWN, Keys.ENTER)

    @allure.step('Заполнение поля Телефон')
    def filling_phone_field(self, phone):
        self.set_text(OrderPageLocators.PHONE, phone)

    @allure.step('Переход на форму Про аренду')
    def click_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение поля Когда привезти самокат')
    def filling_date_field(self, date):
        element = self.find_element(OrderPageLocators.DATE)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    @allure.step('Заполнение поля Срок аренды')
    def filling_rent_field(self):
        self.click_element(OrderPageLocators.RENT_PERIOD)
        self.click_element(OrderPageLocators.CHOOSE_RENTAL_PERIOD)

    @allure.step('Выбор цвета самоката')
    def choose_colour(self, colour_scooter):
        self.click_element(colour_scooter)

    @allure.step('Заполнение комментария')
    def filling_comment_field(self, comment):
        self.set_text(OrderPageLocators.COMMENT, comment)
    
    @allure.step('Подтверждение заказа')
    def confirm(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_IN_FORM)

    @allure.step('Ожидание появления окна с сообщением об успехе')
    def wait_message_success_order(self):
        self.click_element(OrderPageLocators.CONFIRM_YES)
        return self.wait_for_visibility(OrderPageLocators.SUCCESSFUL_ORDER).text


    @allure.step('Заполнение поля формы заказа')
    def set_order_form(self, data, colour_scooter):
        name, surname, address, phone, date, comment = data
        self.filling_name_field(name)
        self.filling_surname_field(surname)
        self.filling_adress_field(address)
        self.filling_metro_field()
        self.filling_phone_field(phone)
        self.click_next()
        self.wait_for_visibility(OrderPageLocators.DATE)
        self.filling_date_field(date)
        self.filling_rent_field()
        self.choose_colour(colour_scooter)
        self.filling_comment_field(comment)
        self.confirm()
        return self.wait_message_success_order()
    