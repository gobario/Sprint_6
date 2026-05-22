from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    URL = "https://qa-scooter.education-services.ru/"

    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_top_order_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.TOP_ORDER_BUTTON)
        ).click()

    def click_bottom_order_button(self):
        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.BOTTOM_ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    def click_question(self, index):
        locator = (By.ID, f"accordion__heading-{index}")

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
         "arguments[0].click();",
          element
        )

    def get_answer_text(self, index):
        locator = (By.ID, f"accordion__panel-{index}")
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).text

    def click_scooter_logo(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.SCOOTER_LOGO)
        ).click()

    def click_yandex_logo(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.YANDEX_LOGO)
        ).click()