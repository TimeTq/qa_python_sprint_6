from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class TrackPage:
    yandex_logo_icon = [By.XPATH, './/a[@class="Header_LogoYandex__3TSOI"]']
    scooter_logo_icon = [By.XPATH, './/a[@class="Header_LogoScooter__3lsAR"]']

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click_yandex_logo_icon(self):
        self.driver.find_element(*self.yandex_logo_icon).click()

    def click_scooter_logo_icon(self):
        self.driver.find_element(*self.scooter_logo_icon).click()
