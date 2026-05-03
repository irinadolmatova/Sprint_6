import allure
import pytest
from locators.order_locators import OrderPageLocators
from pages.order_page import OrderPage
from pages.questions_page import QuestionPage


class TestOrderPage:
    @allure.title('Тест успешного создания заказа по верхней и нижней кнопке Заказать')
    @allure.description('Появления всплывающего окна с сообщением об успешном создании заказа')
    @pytest.mark.parametrize("BUTTON_ORDER, COLOUR_LOCATOR", [
        (OrderPageLocators.HEADER_ORDER_BUTTON, OrderPageLocators.BLACK_COLOUR),
        (OrderPageLocators.HEADER_ORDER_BUTTON, OrderPageLocators.GREY_COLOUR),
        (OrderPageLocators.FOOTER_ORDER_BUTTON, OrderPageLocators.BLACK_COLOUR),
        (OrderPageLocators.FOOTER_ORDER_BUTTON, OrderPageLocators.GREY_COLOUR)
        ])
    def test_order_scooter(self, driver, data_for_order, BUTTON_ORDER, COLOUR_LOCATOR):
        page = OrderPage(driver)
        question_page = QuestionPage(driver)
        question_page.accept_cookies()
        page.push_order_button(BUTTON_ORDER)
        result_text = page.set_order_form(data_for_order, COLOUR_LOCATOR)
        assert "Заказ оформлен" in result_text