import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..data import MAIN_URL


class MainPage(BasePage):
    faq_questions = [By.CLASS_NAME, 'accordion__item']
    faq_questions_answer = [By.XPATH, './/div[@class="accordion__panel" and @hidden=""]']
    faq_question_button = [By.CLASS_NAME, 'accordion__button']
    order_buttons = [
        [By.XPATH, './/div[@class="Header_Nav__AGCXC"]//button[text()="Заказать"]'],
        [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]//button[text()="Заказать"]'],
    ]
    cookies_button = [By.ID, 'rcc-confirm-button']
    yandex_logo_icon = [By.XPATH, './/a[@class="Header_LogoYandex__3TSOI"]']
    scooter_logo_icon = [By.XPATH, './/a[@class="Header_LogoScooter__3lsAR"]']

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Загрузка главной страницы')
    def load_page(self):
        self._get(MAIN_URL)

    @allure.step('Поиск элементов страницы по faq вопросу')
    def get_faq_element_by_question(self, question):
        return [i for i in self._find_elements(self.faq_questions) if i.text == question]

    @allure.step('Поиск ответа faq элемента')
    def get_faq_element_answer(self, faq_element):
        return self._find_element(self.faq_questions_answer, element=faq_element)

    @allure.step('Раскрытие faq элемента')
    def click_faq_question(self, faq_question_element):
        self._click(self.faq_question_button, element=faq_question_element)

    @allure.step('Принятие cookie')
    def click_accept_cookies(self):
        self._click(self.cookies_button)

    @allure.step('Переход по одной из кнопок "Заказать"')
    def click_order_button_by_index(self, button_number_index=0):
        self._click(self.order_buttons[button_number_index])

    @allure.step('Переход по логотипу "Самоката"')
    def click_scooter_logo_icon(self):
        self._click(self.scooter_logo_icon)

    @allure.step('Переход по логотипу "Яндекса"')
    def click_yandex_logo_icon(self):
        self._click(self.yandex_logo_icon)

    @allure.step('Переход по логотипу "Яндекса"')
    def check_dzen_opened(self):
        pass
