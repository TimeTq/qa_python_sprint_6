import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..data import ORDER_PAGE


class OrderPage(BasePage):
    continue_button = [By.XPATH, './/div[@class="Order_NextButton__1_rCA"]/button']
    order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    agree_to_order_button = [By.XPATH, './/div[@class="Order_Modal__YZ-d3"]//button[text()="Да"]']
    watch_status_button = [By.XPATH, './/div[@class="Order_NextButton__1_rCA"]/button']

    name_input = [By.XPATH, './/div[@class="Order_Content__bmtHS"]//input[@placeholder="* Имя"]']
    last_name_input = [By.XPATH, './/div[@class="Order_Content__bmtHS"]//input[@placeholder="* Фамилия"]']
    address_input = [By.XPATH,
                     './/div[@class="Order_Content__bmtHS"]//input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_input = [By.XPATH, './/div[@class="Order_Content__bmtHS"]//input[@placeholder="* Станция метро"]']
    metro_select_button = [By.XPATH, './/div[@class="Order_Text__2broi" and text()="{metro_name}"]/..']
    phone_input = [By.XPATH,
                   './/div[@class="Order_Content__bmtHS"]//input[@placeholder="* Телефон: на него позвонит курьер"]']

    date_to_deliver_input = [By.XPATH,
                             './/div[@class="Order_Form__17u6u"]//input[@placeholder="* Когда привезти самокат"]']
    date_picker_input = [By.XPATH, './/div[@class="react-datepicker__week"]/div']

    rent_time_dropdown = [By.XPATH, './/div[@class="Order_Form__17u6u"]/div[@class="Dropdown-root"]']
    rent_time_dropdown_menu = [By.XPATH, './/div[@class="Order_Form__17u6u"]//div[@class="Dropdown-menu"]']
    rent_time_choose = [By.XPATH, './div[text()="{rent_time}"]']

    scooter_color_checkbox = [By.XPATH, './/div[@class="Order_Form__17u6u"]/div[@class="Order_Checkboxes__3lWSI"]']
    currier_comment_input = [By.XPATH,
                             './/div[@class="Order_Form__17u6u"]//input[@placeholder="Комментарий для курьера"]']

    order_done_div = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']

    label_tag = [By.TAG_NAME, 'label']
    input_tag = [By.TAG_NAME, 'input']

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Загрузка страницы заказа')
    def load_page(self):
        self._get(ORDER_PAGE)

    @allure.step('Клик по кнопке "Продолжить"')
    def click_continue_button(self):
        self._click(self.continue_button)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self._click(self.order_button)

    @allure.step('Клик по кнопке "Да"')
    def click_agree_to_order_button(self):
        self._click(self.agree_to_order_button)

    @allure.step('Клик по кнопке "Посмотреть статус"')
    def click_watch_status_button(self):
        self._click(self.watch_status_button)

    @allure.step('Заполнение имени')
    def set_name(self, value):
        self._send_keys(self.name_input, value)

    @allure.step('Заполнение фамилии')
    def set_last_name(self, value):
        self._send_keys(self.last_name_input, value)

    @allure.step('Заполнение адреса заказа')
    def set_address(self, value):
        self._send_keys(self.address_input, value)

    @allure.step('Заполнение станции метро')
    def set_metro(self, value):
        self._send_keys(self.metro_input, value)

        by, metro_button_locator = self.metro_select_button
        self._click([by, metro_button_locator.format(metro_name=value)])

    @allure.step('Заполнение номера телефона')
    def set_phone(self, value):
        self._send_keys(self.phone_input, value)

    @allure.step('Заполнение даты заказа')
    def set_date_to_deliver(self):
        self._click(self.date_to_deliver_input)
        self._click(self.date_picker_input)

    @allure.step('Заполнение продолжительности заказа')
    def set_rent_time(self, value):
        self._click(self.rent_time_dropdown)

        dropdown = self._find_element(self.rent_time_dropdown_menu)
        by, rent_time = self.rent_time_choose
        self._click([by, rent_time.format(rent_time=value)], element=dropdown)

    @allure.step('Заполнение цвета самоката')
    def set_scooter_color(self, value):
        colors_check_box = self._find_element(self.scooter_color_checkbox)
        for checkbox in self._find_elements(self.label_tag, element=colors_check_box):
            if checkbox.text == value:
                self._click(self.input_tag, element=checkbox)

    @allure.step('Заполнение комментария курьеру')
    def set_currier_comment(self, value):
        self._send_keys(self.currier_comment_input, value)
    
    @allure.step('Заполнение информации о заказчике')
    def set_user_info(self, name, last_name, address, metro, phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)

    @allure.step('Заполнение информации о доставке')
    def set_rent_info(self, rent_time, scooter_color, currier_comment):
        self.set_date_to_deliver()
        self.set_rent_time(rent_time)
        self.set_scooter_color(scooter_color)
        self.set_currier_comment(currier_comment)

    @allure.step('Проверка успешности заказа')
    def check_success_order_message(self):
        order_done = self._find_element(self.order_done_div)
        assert order_done.text.startswith('Заказ оформлен')
