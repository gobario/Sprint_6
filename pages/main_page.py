import allure
from selenium.webdriver.common.by import By

from data.urls import BASE_URL
from pages.base_page import BasePage


class MainPage(BasePage):

    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(BASE_URL)

    @allure.step("Кликнуть по верхней кнопке Заказать")
    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть по нижней кнопке Заказать")
    def click_bottom_order_button(self):
        self.js_click_element(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликнуть по вопросу в FAQ")
    def click_question(self, index):
        locator = (By.ID, f"accordion__heading-{index}")
        self.js_click_element(locator)

    @allure.step("Получить текст ответа в FAQ")
    def get_answer_text(self, index):
        locator = (By.ID, f"accordion__panel-{index}")
        return self.get_text(locator)

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Переключиться на новое окно после клика по логотипу Яндекса")
    def switch_to_yandex_window(self, old_window):
        self.wait_new_window_and_switch(old_window)

    @allure.step("Получить текущее окно")
    def get_current_window_handle(self):
        return self.get_current_window()

    @allure.step("Дождаться загрузки страницы Яндекса или Дзена")
    def wait_yandex_or_dzen_page_loaded(self):
        self.wait_url_is_not_blank()

    @allure.step("Проверить, что открыт Яндекс или Дзен")
    def is_yandex_or_dzen_opened(self):
        current_url = self.get_current_url().lower()
        return "yandex" in current_url or "dzen" in current_url

    @allure.step("Проверить, что открыта главная страница Самоката")
    def is_main_page_opened(self):
        return self.get_current_url() == BASE_URL