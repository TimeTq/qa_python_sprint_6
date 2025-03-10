import allure
import pytest
from selenium import webdriver

from ..data import MAIN_URL
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

    question_answer = {
        'Сколько это стоит? И как оплатить?':
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Хочу сразу несколько самокатов! Так можно?':
            'Пока что у нас так: один заказ — один самокат. '
            'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'Как рассчитывается время аренды?':
            'Допустим, вы оформляете заказ на 8 мая. '
            'Мы привозим самокат 8 мая в течение дня. '
            'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
            'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'Можно ли заказать самокат прямо на сегодня?':
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Можно ли продлить заказ или вернуть самокат раньше?':
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Вы привозите зарядку вместе с самокатом?':
            'Самокат приезжает к вам с полной зарядкой. '
            'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
            'Зарядка не понадобится.',
        'Можно ли отменить заказ?':
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Я жизу за МКАДом, привезёте?':
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
    }

    @allure.step('В разделе «Вопросы о важном», когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize('question, answer', question_answer.items())
    def test_faq_question_click_question_answer_is_displayed_answer(self, question, answer):
        faq_question_elements = self.main_page.get_faq_element_by_question(question)
        assert len(faq_question_elements) == 1, \
            f'Count of elements with faq question {question!r} equals {len(faq_question_elements)}'

        faq_question_element = faq_question_elements[0]

        faq_answer = self.main_page.get_faq_element_answer(faq_question_element)
        assert not faq_answer.is_displayed(), 'FAQ answer is displayed before click'

        self.main_page.click_faq_question(faq_question_element)
        assert faq_answer.is_displayed(), 'FAQ answer is not displayed after click'
        assert faq_answer.text == answer, f'FAQ answer ({faq_answer.text}) is not equal tested answer {answer}'
