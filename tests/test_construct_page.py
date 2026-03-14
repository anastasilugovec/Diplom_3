from pages.base_page import BasePage
from pages.construct_page import Construct
import pytest
import allure

class TestConstructPage():
    @allure.title("Проверка перехода в Конструктор через кнопку в шапке сайта")
    def test_construct_button_click(self, driver, urls):
        base_page = BasePage(driver)
        base_page.get_urls(urls.STELLAR_BURGER_LENTA)
        base_page.click_construct_button()
        construct_page = Construct(driver)
        assert construct_page.is_burger_constructor_displayed()

    @allure.title("Проверка открытия модального окна с деталями ингредиента")
    def test_window_ingridient_in_display(self, driver, urls):
        construct_page = Construct(driver)
        construct_page.get_urls(urls.STELLAR_BURGER_CONSTRUCT)
        construct_page.wait_for_ingredients_loaded()
        construct_page.open_ingredient_details()
        construct_page.wait_for_ingredient_window()
        assert construct_page.is_ingredient_window_displayed()

    @allure.title("Проверка закрытия модального окна ингредиента кликом на крестик")
    def test_close_window_ingridient_click_the_cross(self, driver, urls):
        construct_page = Construct(driver)
        construct_page.get_urls(urls.STELLAR_BURGER_CONSTRUCT)
        # Увеличиваем тайм-аут ожидания до 15 секунд
        construct_page.wait_for_ingredients_loaded(timeout=15)
        construct_page.open_ingredient_details()
        close_button = construct_page.get_close_button()
        construct_page.close_ingredient_details()
        # Используем новый метод для ожидания исчезновения окна
        construct_page.wait_for_ingredient_window_to_disappear()
        class_name = close_button.get_attribute("class")
        assert "Modal_modal_opened__3ISw4" not in class_name

    @allure.title("Проверка добавления ингредиента в конструктор заказа")
    def test_ingredient_added_to_an_order(self, driver, urls):
        construct_page = Construct(driver)
        construct_page.get_urls(urls.STELLAR_BURGER_CONSTRUCT)
        construct_page.add_ingredient_to_constructor()
        counter = construct_page.get_ingredient_counter()
        construct_page.wait()
        assert counter == "2"