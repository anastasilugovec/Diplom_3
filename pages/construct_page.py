import allure
from locators.construct_page_locators import ConstructPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Construct(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

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
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(ConstructPageLocators.BUN_INGRIDIENT))
        wait.until(EC.element_to_be_clickable(ConstructPageLocators.BUN_INGRIDIENT))

    @allure.step("Ожидать изменения номера заказа")
    def wait_for_order_number_changed(self, initial_number):
        self.wait_text_changed(ConstructPageLocators.NUMBER_ORDER, initial_number)

    @allure.step("Ожидать окно ингредиента")
    def wait_for_ingredient_window(self):
        self.wait_element(ConstructPageLocators.WINDOW_INGRIDIENT)

    @allure.step("Проверить отображение окна ингредиента")
    def is_ingredient_window_displayed(self):
        return self.element_is_displayed(ConstructPageLocators.WINDOW_INGRIDIENT)

    @allure.step("Получить элемент крестика закрытия")
    def get_close_button(self):
        return self.find_element(ConstructPageLocators.WINDOW_CROSS)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(ConstructPageLocators.BUN_INGRIDIENT, ConstructPageLocators.BURGER_ORDER_LIST)

    @allure.step("Нажать кнопку 'Конструктор'")
    def click_construct_button(self):
        self.click_to_element_js(BasePageLocators.BUTTON_CONSTRUCT)

    @allure.step("Нажать кнопку 'Лента заказов'")
    def click_lenta_button(self):
        self.click_to_element_js(BasePageLocators.LENTA_ORDERS)

    @allure.step("Ожидать кликабельности кнопки 'Лента заказов'")
    def wait_lenta_button_clickable(self):
        self.wait_element_clickable(BasePageLocators.LENTA_ORDERS)

    # Новый метод для ожидания исчезновения окна ингредиента
    def wait_for_ingredient_window_to_disappear(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(ConstructPageLocators.WINDOW_INGRIDIENT))