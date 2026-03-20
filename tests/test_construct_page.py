from pages.base_page import BasePage
from pages.construct_page import Construct
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.construct_page_locators import ConstructPageLocators
from urls import Urls  # Импортируйте класс Urls из модуля urls

class TestConstructPage:

    @allure.title("Проверка перехода в Конструктор через кнопку в шапке сайта")
    def test_construct_button_click(self, driver):
        urls = Urls()
        construct_page = Construct(driver)
        construct_page.get_urls(urls.STELLAR_BURGER_LENTA)
        construct_page.click_construct_button()
        assert construct_page.is_burger_constructor_displayed()

    @allure.title("Проверка открытия модального окна с деталями ингредиента")
    def test_window_ingridient_in_display(self, driver):
        urls = Urls()
        construct_page = Construct(driver)
        construct_page.get_urls(urls.STELLAR_BURGER_CONSTRUCT)
        construct_page.wait_for_ingredients_loaded()
        construct_page.open_ingredient_details()
        construct_page.wait_for_ingredient_window()
        assert construct_page.is_ingredient_window_displayed()

    @allure.title("Проверка закрытия модального окна ингредиента кликом на крестик")
    def test_close_window_ingridient_click_the_cross(self, driver):
        urls = Urls()
        construct_page = Construct(driver)
        construct_page.get_urls(urls.STELLAR_BURGER_CONSTRUCT)
        construct_page.wait_for_ingredients_loaded(timeout=15)
        construct_page.open_ingredient_details()

        construct_page.close_modal()

        construct_page.wait_for_ingredient_window_to_disappear()

        close_button = construct_page.get_close_button()

        assert close_button is None, "Кнопка закрытия должна быть недоступна после закрытия окна"

    @allure.title("Проверка добавления ингредиента в конструктор заказа")
    def test_ingredient_added_to_an_order(self, driver):
        urls = Urls()
        construct_page = Construct(driver)
        construct_page.get_urls(urls.STELLAR_BURGER_CONSTRUCT)
        construct_page.add_ingredient_to_constructor()
        counter = construct_page.get_ingredient_counter()
        assert counter == "2"