import allure
import pytest
from selenium import webdriver

from ..data import MAIN_URL, FAQ_QUESTION_ANSWER
from ..pages.main_page import MainPage


class TestMainPageFaqQuestion:
    driver = None
    main_page = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(MAIN_URL)
        cls.main_page = MainPage(cls.driver)
        cls.main_page.click_accept_cookies()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('В разделе «Вопросы о важном», когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize('question, answer', FAQ_QUESTION_ANSWER.items())
    def test_faq_question_click_question_answer_is_displayed_answer(self, question, answer):
        faq_question_element = self.main_page.get_faq_element_by_question(question)[0]
        faq_answer = self.main_page.get_faq_element_answer(faq_question_element)

        self.main_page.click_faq_question(faq_question_element)
        assert faq_answer.is_displayed(), 'FAQ answer is not displayed after click'
        assert faq_answer.text == answer, f'FAQ answer ({faq_answer.text}) is not equal tested answer {answer}'
