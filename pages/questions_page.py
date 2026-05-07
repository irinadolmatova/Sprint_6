import allure
from pages.base_page import BasePage
from locators.questions_locators import QuestionPageLocators

class QuestionPage(BasePage):

    @allure.step('Проверяем текущий URL')
    def check_open_page(self):
        return self.get_current_url()
    
    @allure.step('Скролл до раздела Вопросы о важном')
    def scroll_to_questions(self):
        self.scroll_to_element(QuestionPageLocators.QUESTIONS_ABOUT_IMPORTANT)

    @allure.step('Клик на вопрос')
    def find_question(self, question_locator):
        self.click_element(question_locator)

    @allure.step('Получение ответа')
    def get_text(self, answer_locator):
        element = self.wait_for_visibility(answer_locator)
        return element.text

    @allure.step('Получение ответа на выбранный вопрос')
    def get_faq_answer(self, question_locator, answer_locator):
        self.scroll_to_important()
        self.click_question(question_locator)
        return self.get_answer_text(answer_locator)