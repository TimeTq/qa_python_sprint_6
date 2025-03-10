from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    faq_questions = [By.CLASS_NAME, 'accordion__item']
    faq_questions_answer = [By.XPATH, './/div[@class="accordion__panel" and @hidden=""]']
    faq_question_button = [By.CLASS_NAME, 'accordion__button']
    order_buttons = [
        [By.XPATH, './/button[text()="Заказать"]'],
        [By.XPATH, './/button[text()="Заказать"]'],
    ]
    cookies_button = [By.ID, 'rcc-confirm-button']

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait_timer = 3
        self.wait = WebDriverWait(self.driver, timeout=self.wait_timer)

    def get_faq_element_by_question(self, question):
        return [i for i in self.driver.find_elements(*self.faq_questions) if i.text == question]

    def get_faq_element_answer(self, faq_element):
        return faq_element.find_element(*self.faq_questions_answer)

    def click_faq_question(self, faq_question_element):
        faq_button = faq_question_element.find_element(*self.faq_question_button)
        faq_button.click()

    def click_accept_cookies(self):
        self.driver.find_element(*self.cookies_button).click()

    def click_order_button_by_index(self, button_number_index=0):
        self.driver.find_element(*self.order_buttons[button_number_index]).click()

    def check_redirection_to_order_page(self, order_page_url):
        start_url = self.driver.current_url
        for order_button in self.driver.find_elements(*self.order_buttons):
            order_button.click()
            self.wait.until(
                EC.url_to_be(order_page_url),
                message=f'Redirrected url not equal target url {order_page_url!r} after {self.wait_timer} sec'
            )

            self.driver.get(start_url)
