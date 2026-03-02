import pytest
import allure
from pages.home_page import HomePage
from pages.constructor_page import ConstructorPage
from pages.order_page import OrderPage

@allure.feature("Основной функционал")
def test_navigation_to_constructor(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_constructor()
    assert "Конструктор" in driver.title

@allure.feature("Основной функционал")
def test_navigation_to_order_list(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_order_list()
    assert "Лента заказов" in driver.title

@allure.story("Детали ингредиента")
def test_ingredient_details_modal(driver):
    home = HomePage(driver)
    home.open()
    constr = ConstructorPage(driver)
    home.go_to_constructor()
    constr.open_ingredient_details("Булка")
    assert constr.is_modal_open()
    constr.close_modal()
    assert not constr.is_modal_open()

@allure.story("Добавление ингредиента")
def test_add_ingredient_increases_counter(driver):
    home = HomePage(driver)
    home.open()
    constr = ConstructorPage(driver)
    home.go_to_constructor()
    initial_count = constr.get_ingredient_counter("Булка")
    constr.add_ingredient_to_order("Булка")
    new_count = constr.get_ingredient_counter("Булка")
    assert new_count == initial_count + 1

@allure.story("Создание заказа и проверка счетчиков")
def test_create_order_and_check_counts(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_constructor()
    constr = ConstructorPage(driver)
    constr.add_ingredient_to_order("Булка")
    home.go_to_order_list()
    order_page = OrderPage(driver)
    initial_total = order_page.get_total_completed_count()
    initial_today = order_page.get_today_completed_count()

    # Создаем заказ
    home.go_to_constructor()
    constr = ConstructorPage(driver)
    constr.add_ingredient_to_order("Булка")
    order_page.create_order()

    # Проверка увеличения счетчиков
    assert order_page.get_total_completed_count() == initial_total + 1
    assert order_page.get_today_completed_count() == initial_today + 1

    # Проверка, что заказ появился в разделе «В работе»
    order_number = order_page.get_current_order_number()
    home.go_to_order_list()
    assert order_page.is_order_in_work(order_number)