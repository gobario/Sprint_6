import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):

    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_POPUP = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")

    @allure.step("Заполнить первую форму заказа")
    def fill_first_order_form(self, name, surname, address, metro, phone):
        self.fill_input(self.NAME_INPUT, name)
        self.fill_input(self.SURNAME_INPUT, surname)
        self.fill_input(self.ADDRESS_INPUT, address)

        metro_field = self.find_visible_element(self.METRO_INPUT)
        metro_field.send_keys(metro)
        metro_field.send_keys(Keys.ARROW_DOWN)
        metro_field.send_keys(Keys.ENTER)

        self.fill_input(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_order_form(self, date, rent_period, comment):
        date_field = self.find_visible_element(self.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.click_element(self.RENT_DROPDOWN)

        rent_period_locator = (By.XPATH, f".//div[text()='{rent_period}']")
        self.click_element(rent_period_locator)

        self.click_element(self.BLACK_COLOR_CHECKBOX)
        self.fill_input(self.COMMENT_INPUT, comment)
        self.click_element(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(self.CONFIRM_BUTTON)

    @allure.step("Проверить, что появился попап успешного заказа")
    def is_success_popup_displayed(self):
        return self.find_visible_element(self.SUCCESS_POPUP).is_displayed()