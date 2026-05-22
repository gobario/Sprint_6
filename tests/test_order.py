import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, rent_period, comment, order_button",
        [
            (
                "Иван",
                "Иванов",
                "Москва, Ленина 1",
                "Сокольники",
                "+79991234567",
                "25.05.2026",
                "сутки",
                "Позвонить заранее",
                "top",
            ),
            (
                "Пётр",
                "Петров",
                "Москва, Пушкина 10",
                "Черкизовская",
                "+79997654321",
                "26.05.2026",
                "двое суток",
                "Оставить у подъезда",
                "bottom",
            ),
        ]
    )
    @allure.title("Позитивный сценарий заказа самоката")
    def test_create_order_positive_scenario(
        self,
        driver,
        name,
        surname,
        address,
        metro,
        phone,
        date,
        rent_period,
        comment,
        order_button,
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()

        if order_button == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_first_order_form(name, surname, address, metro, phone)
        order_page.fill_second_order_form(date, rent_period, comment)
        order_page.confirm_order()

        assert order_page.is_success_popup_displayed()


class TestLogo:

    @allure.title("Переход на главную страницу по логотипу Самоката")
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_top_order_button()
        main_page.click_scooter_logo()

        assert main_page.is_main_page_opened()

    @allure.title("Переход на Дзен по логотипу Яндекса")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()

        old_window = main_page.get_current_window_handle()

        main_page.click_yandex_logo()
        main_page.switch_to_yandex_window(old_window)
        main_page.wait_yandex_or_dzen_page_loaded()

        assert main_page.is_yandex_or_dzen_opened()