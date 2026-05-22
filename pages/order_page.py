from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
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

    def __init__(self, driver):
        self.driver = driver

    def fill_first_order_form(self, name, surname, address, metro, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

        metro_field = self.driver.find_element(*self.METRO_INPUT)
        metro_field.send_keys(metro)
        metro_field.send_keys(Keys.ARROW_DOWN)
        metro_field.send_keys(Keys.ENTER)

        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_second_order_form(self, date, rent_period, comment):
        date_field = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.DATE_INPUT)
        )
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.driver.find_element(*self.RENT_DROPDOWN).click()
        self.driver.find_element(By.XPATH, f".//div[text()='{rent_period}']").click()

        self.driver.find_element(*self.BLACK_COLOR_CHECKBOX).click()
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        ).click()

    def is_success_popup_displayed(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SUCCESS_POPUP)
        ).is_displayed()