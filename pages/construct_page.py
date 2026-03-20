import allure
from locators.construct_page_locators import ConstructPageLocators
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Construct(BasePage):

    @allure.step("Создание заказа бургера")
    def create_order_burger(self, element):
        self.drag_and_drop(element, ConstructPageLocators.BURGER_ORDER_LIST)
        self.click_to_element(ConstructPageLocators.BUTTON_ORDER)

    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self):
        self.click_to_element_js(ConstructPageLocators.BUN_INGRIDIENT)

    @allure.step("Закрыть окно деталей ингредиента")
    def close_ingredient_details(self):
        self.click_to_element_js(ConstructPageLocators.WINDOW_CROSS)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        return self.find_element(ConstructPageLocators.BUN_COUNTER).text

    @allure.step("Ожидание появления номера заказа")
    def wait_for_order_number(self):
        self.wait_element(ConstructPageLocators.NUMBER_ORDER)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.find_element(ConstructPageLocators.NUMBER_ORDER).text

    @allure.step("Закрыть окно заказа")
    def close_order_window(self):
        self.click_to_element_js(ConstructPageLocators.CLOSE_BUTTON_ORDER_WINDOW)

    @allure.step("Добавить булку в заказ")
    def add_bun_to_order(self):
        self.create_order_burger(ConstructPageLocators.BUN_INGRIDIENT)

    @allure.step("Проверить отображение текста конструктора")
    def is_burger_constructor_displayed(self):
        return self.element_is_displayed(ConstructPageLocators.TEXT_BURGER_CONSTRUCT)

    @allure.step("Ожидать загрузки ингредиентов")
    def wait_for_ingredients_loaded(self, timeout=10):
        self.wait_element(ConstructPageLocators.BUN_INGRIDIENT, timeout)
        self.wait_element_clickable(ConstructPageLocators.BUN_INGRIDIENT, timeout)

    @allure.step("Ожидать изменения номера заказа")
    def wait_for_order_number_changed(self, initial_number):
        self.wait_text_changed(ConstructPageLocators.NUMBER_ORDER, initial_number)

    @allure.step("Ожидать окно ингредиента")
    def wait_for_ingredient_window(self):
        self.wait_element(ConstructPageLocators.WINDOW_INGRIDIENT)

    @allure.step("Ожидать исчезновения окна ингредиента")
    def wait_for_ingredient_window_to_disappear(self, timeout=10):
        self.wait_invisibility(ConstructPageLocators.WINDOW_INGRIDIENT, timeout)

    @allure.step("Проверить отображение окна ингредиента")
    def is_ingredient_window_displayed(self):
        return self.element_is_displayed(ConstructPageLocators.WINDOW_INGRIDIENT)

    @allure.step("Получение кнопки закрытия окна")
    def get_close_button(self):
        try:
            return self.find_element_with_wait(ConstructPageLocators.WINDOW_CROSS, timeout=30)
        except TimeoutException:
            return None

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(ConstructPageLocators.BUN_INGRIDIENT, ConstructPageLocators.BURGER_ORDER_LIST)

    @allure.step("Нажать кнопку 'Конструктор'")
    def click_construct_button(self):
        self.click_to_element_js(BasePageLocators.BUTTON_CONSTRUCT)

    @allure.step("Нажать кнопку 'Лента заказов'")
    def click_lenta_button(self):
        self.click_to_element_js(ConstructPageLocators.LENTA_ORDERS)

    @allure.step("Ожидать кликабельности кнопки 'Лента заказов'")
    def wait_lenta_button_clickable(self):
        self.wait_element_clickable(ConstructPageLocators.LENTA_ORDERS)

    @allure.step("Ожидание {seconds} секунд")
    def wait_for_time(self, seconds):
        wait = WebDriverWait(self.driver, seconds)
        wait.until(lambda driver: True)

    @allure.step("Ожидание исчезновения окна с ингредиентами")
    def wait_for_ingredient_window_to_disappear(self, timeout=10):
        self.wait_invisibility(ConstructPageLocators.WINDOW_INGRIDIENT, timeout)

    @allure.step("Выбрать бургер")
    def select_burger(self):
        self.click(BasePageLocators.BURGER)

    @allure.step("Заполнить форму данными: {data}")
    def fill_form(self, data):
        self.send_keys(BasePageLocators.NAME_FIELD, data['name'])
        self.send_keys(BasePageLocators.ADDRESS_FIELD, data['address'])

    @allure.step("Нажатие безопасной кнопки Лента с помощью JS")
    def click_lenta_button_js_safe(self):
        self.driver.execute_script("arguments[0].click();", self.find_element(ConstructPageLocators.LENTA_ORDERS))

    @allure.step("Обновление страницы")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Ожидаем, пока URL содержит: {url_part}")
    def wait_for_url_contains(self, url_part, timeout=10):
        self.wait_url(url_part, timeout=timeout)

    @allure.step("Закрываем модальное окно через JavaScript")
    def close_modal(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(ConstructPageLocators.WINDOW_CROSS))
        self.click_to_element_js(ConstructPageLocators.WINDOW_CROSS)

