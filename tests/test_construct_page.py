import pytest
import allure


class TestLentaPage():

    @allure.title("Проверка, что заказ появляется в списке 'В работе' после создания")
    def test_order_appears_in_work_list(self, driver, login_user, urls):
        profile_page = Profile(driver)
        construct_page = Construct(driver)
        lenta_page = Lenta(driver)

        # Открываем страницу конструктора и логинимся
        construct_page.open(urls.STELLAR_BURGER_CONSTRUCT)
        profile_page.login_in_main_page(login_user["email"], login_user["password"])

        # Создаем заказ
        construct_page.add_bun_to_order()
        construct_page.wait_for_order_number()
        construct_page.close_order_window()

        # Переходим в ленту заказов
        construct_page.wait_lenta_button_clickable()
        construct_page.click_lenta_button_js_safe()
        construct_page.wait_for_url(urls.STELLAR_BURGER_LENTA)

        # Обновляем страницу и ждем
        construct_page.refresh_page()
        construct_page.wait_for_time(8)

        # Скроллим к списку заказов
        lenta_page.scroll_to_order_list()
        construct_page.wait_for_time(2)

        # Получаем список заказов
        orders_after = lenta_page.get_order_list()

        # Проверка: есть хотя бы один заказ
        assert len(orders_after) > 0, "Заказ не добавлен в список 'В работе'"

        # Проверяем, что номер заказа состоит только из цифр
        latest_order = orders_after[0]
        assert latest_order.isdigit(), f"Номер заказа должен содержать только цифры: {latest_order}"