from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait_timer = 3
        self.wait = WebDriverWait(self.driver, timeout=self.wait_timer)

    @property
    def current_url(self):
        return self.driver.current_url

    def _get(self, url):
        return self.driver.get(url)

    def _click(self, locator, element=None):
        click_element = self._find_element(locator, element)

        self.wait.until(EC.element_to_be_clickable(click_element))
        click_element.click()

    def _find_element(self, locator, element=None):
        if element is not None:
            return element.find_element(*locator)

        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def _find_elements(self, locator, element=None):
        if element is not None:
            return element.find_elements(*locator)

        return self.driver.find_elements(*locator)

    def _send_keys(self, locator, value, element=None):
        return self._find_element(locator, element).send_keys(value)

    def switch_to_new_page(self, expected_url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(lambda driver: driver.current_url.startswith(expected_url))
