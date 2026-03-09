from pages.base_page import BasePage
from pages.construct_page import Construct
from pages.profile_page import Profile
from pages.lenta_page import Lenta
import pytest
import allure

class TestLentaPage:
    @pytest.mark.parametrize("counter_method", ["get_all_time_order_count", "get_today_order_count"])
    @allure.title("Проверка увеличения счетчика заказов после создания нового заказа")
    def test_order_counter_increases_after_order(self, driver, login_user, urls, counter_method):
        # Создаем страницы нужных классов
        profile_page = Profile(driver)
        construct_page = Construct(driver)
        lenta_page = Lenta(driver)

        # Открываем страницу ленты
        lenta_page.open(urls.STELLAR_BURGER_LENTA)

        # Получаем счетчик до создания заказа
        count_before = getattr(lenta_page, counter_method)()

        # Создаем заказ
        construct_page.click_construct_button()
        profile_page.login_in_main_page(login_user["email"], login_user["password"])
        construct_page.add_bun_to_order()
        construct_page.wait_for_order_number()
        construct_page.close_order_window()

        # Обновляем страницу и ждем
        construct_page.wait_for_time(10)
        construct_page.refresh_page()
        construct_page.wait_for_time(3)

        # Получаем счетчик после
        count_after = getattr(lenta_page, counter_method)()

        # Проверка
        assert count_after > count_before, (
            f"Счетчик '{counter_method}' не увеличился: было {count_before}, стало {count_after}."
        )

    @pytest.mark.parametrize("login_user, urls", [
        ({"email": "test@example.com", "password": "password123"}, {"STELLAR_BURGER_CONSTRUCT": "...", "STELLAR_BURGER_LENTA": "..."}) # замените на реальные URL
    ])
    @allure.title("Проверка добавления номера заказа в список 'В работе'")
    def test_order_adds_to_in_progress_list(self, driver, login_user, urls):
        profile_page = Profile(driver)
        construct_page = Construct(driver)
        lenta_page = Lenta(driver)

        # Зайти на страницу конструктора и авторизоваться
        construct_page.open(urls["STELLAR_BURGER_CONSTRUCT"])
        profile_page.login_in_main_page(login_user["email"], login_user["password"])

        # Создать заказ
        construct_page.add_bun_to_order()
        construct_page.wait_for_order_number()
        construct_page.close_order_window()

        # Ждать и перейти в ленту заказов
        construct_page.wait_for_time(3)
        construct_page.wait_lenta_button_clickable()
        construct_page.click_lenta_button_js_safe()
        construct_page.wait_for_url(urls["STELLAR_BURGER_LENTA"])

        # Обновляем страницу
        construct_page.wait_for_time(8)
        construct_page.refresh_page()
        construct_page.wait_for_time(8)

        # Проверка, что мы на нужной странице
        current_url = construct_page.get_current_url()
        assert current_url == urls["STELLAR_BURGER_LENTA"], f"Неверный URL: {current_url}"

        # Скроллим к списку заказов
        lenta_page.scroll_to_order_list()
        construct_page.wait_for_time(2)

        # Получаем список заказов
        orders_after = lenta_page.get_order_list()

        # Проверка, что заказ появился
        assert len(orders_after) > 0, "Заказ не добавлен в список 'В работе'"

        # Проверка, что номер заказа состоит только из цифр
        latest_order = orders_after[0]
        assert latest_order.isdigit(), f"Номер заказа должен содержать только цифры: {latest_order}"

        print(f"Заказ {latest_order} успешно добавлен в список 'В работе'")