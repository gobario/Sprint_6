import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step("Кликнуть по элементу через JS")
    def js_click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнить поле")
    def fill_input(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def wait_new_window_and_switch(self, old_window, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > 1
        )

        new_window = [
            window for window in self.driver.window_handles
            if window != old_window
        ][0]

        self.driver.switch_to.window(new_window)

    def get_current_window(self):
        return self.driver.current_window_handle

    def wait_url_is_not_blank(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url != "about:blank"
        )