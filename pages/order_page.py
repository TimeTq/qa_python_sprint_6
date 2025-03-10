from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class OrderPage:
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


    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait_timer = 3
        self.wait = WebDriverWait(self.driver, timeout=self.wait_timer)

    def _click_button(self, locator: list[str]):
        self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def click_continue_button(self):
        self._click_button(self.continue_button)

    def click_order_button(self):
        self._click_button(self.order_button)

    def click_agree_to_order_button(self):
        self._click_button(self.agree_to_order_button)

    def click_watch_status_button(self):
        self._click_button(self.watch_status_button)

    def set_name(self, value):
        self.driver.find_element(*self.name_input).send_keys(value)

    def set_last_name(self, value):
        self.driver.find_element(*self.last_name_input).send_keys(value)

    def set_address(self, value):
        self.driver.find_element(*self.address_input).send_keys(value)

    def set_metro(self, value):
        self.driver.find_element(*self.metro_input).send_keys(value)

        by, metro_button_locator = self.metro_select_button
        self.driver.find_element(by, metro_button_locator.format(metro_name=value)).click()

    def set_phone(self, value):
        self.driver.find_element(*self.phone_input).send_keys(value)

    def set_date_to_deliver(self):
        self.driver.find_element(*self.date_to_deliver_input).click()
        self.driver.find_elements(*self.date_picker_input)[0].click()

    def set_rent_time(self, value):
        input_form = self.driver.find_element(*self.rent_time_dropdown)
        input_form.click()

        dropdown = self.driver.find_element(*self.rent_time_dropdown_menu)
        self.wait.until(EC.element_to_be_clickable(dropdown))

        by, rent_time = self.rent_time_choose
        dropdown.find_element(by, rent_time.format(rent_time=value)).click()

    def set_scooter_color(self, value):
        colors_check_box = self.driver.find_element(*self.scooter_color_checkbox)
        for checkbox in colors_check_box.find_elements(By.TAG_NAME, 'label'):
            if checkbox.text == value:
                checkbox.find_element(By.TAG_NAME, 'input').click()

    def set_currier_comment(self, value):
        self.driver.find_element(*self.currier_comment_input).send_keys(value)

    def set_user_info(self, name, last_name, address, metro, phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)

    def set_rent_info(self, rent_time, scooter_color, currier_comment):
        self.set_date_to_deliver()
        self.set_rent_time(rent_time)
        self.set_scooter_color(scooter_color)
        self.set_currier_comment(currier_comment)

    def check_success_order_message(self):
        self.wait.until(EC.visibility_of_element_located(self.order_done_div))
        order_done = self.driver.find_element(*self.order_done_div)
        assert order_done.text.startswith('Заказ оформлен')
