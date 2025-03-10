import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from ..data import MAIN_URL, DZEN_URL, DZEN_REDIRECT_URL
from ..pages.main_page import MainPage
from ..pages.order_page import OrderPage


class TestOrderScooter:
    driver = None
    wait = None
    main_page = None
    order_page = None
    track_page = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, timeout=3)

        cls.main_page = MainPage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

        cls.driver.get(MAIN_URL)
        cls.main_page.click_accept_cookies()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    order_flow_data = [
        [
            0,
            ['имяодин', 'фамилияодин', 'адресодин', 'Университет', 11111111111],
            ['сутки', 'чёрный жемчуг', 'комментарий 1'],
        ],
        [
            1,
            ['имядва', 'фамилиядва', 'адресдва', 'Комсомольская', 22222222222],
            ['сутки', 'серая безысходность', 'комментарий 2'],
        ],
    ]

    @pytest.mark.parametrize('order_button_index, user_info, rent_info', order_flow_data)
    @allure.title('Проверить весь путь заказа самоката позитивного сценария с двумя наборами данных')
    def test_correct_order_buttons_redirection_none_url_is_order_page(self, order_button_index, user_info, rent_info):
        self.driver.get(MAIN_URL)

        # Нажать кнопку «Заказать». На странице две кнопки заказа.
        self.main_page.click_order_button_by_index(order_button_index)

        # Заполнить форму заказа.
        self.order_page.set_user_info(*user_info)
        self.order_page.click_continue_button()

        self.order_page.set_rent_info(*rent_info)
        self.order_page.click_order_button()
        self.order_page.click_agree_to_order_button()

        # Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
        self.order_page.check_success_order_message()

    @allure.title('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_click_scooter_logo_none_url_is_main_page(self):
        self.main_page.load_page()
        self.main_page.click_scooter_logo_icon()
        assert self.main_page.current_url == MAIN_URL

    @allure.title('Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_click_yandex_logo_none_url_is_dzen_page(self):
        self.main_page.load_page()
        self.main_page.click_yandex_logo_icon()

        self.main_page.switch_to_new_page(DZEN_URL)
        assert self.main_page.current_url == DZEN_REDIRECT_URL
