from selenium.webdriver.common.by import By
import allure
from locators.construct_page_locators import ConstructPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class Profile(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Логин на главной странице")
    def login_in_main_page(self, email, password):
        self.click_to_element_js(ConstructPageLocators.BUTTON_IN_ACCOUNT)
        self.send_keys_to_element(ProfilePageLocators.EMAIL_INPUT, email)
        self.send_keys_to_element(ProfilePageLocators.PASSWORD_INPUT, password)
        self.click_to_element(ProfilePageLocators.BUTTON_LOGIN)
        self.wait_element(ConstructPageLocators.BUTTON_ORDER)

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

    def send_keys_to_element(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)