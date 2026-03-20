import allure
import logging
from locators.lenta_page_locators import LentaPageLocators
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By
from logger import logger
from locators.lenta_page_locators import LentaPageLocators

class Lenta(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = LentaPageLocators()

    @allure.step("Получение общего количества заказов за всё время")
    def get_all_time_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_ALL_TIME)
        count_text = self.find_element(LentaPageLocators.COUNT_ALL_TIME).text
        return int(count_text)

    @allure.step("Получить список номеров заказов")
    def get_order_list(self):
        orders = []
        try:
            elements = self.find_elements(self.locators.LIST_ORDER)
            if elements:
                orders = [order.text for order in elements if order.text.strip() and order.text.strip().isdigit()]
                logger.info(f"Найдено заказов: {len(orders)}")
                return orders
            else:
                logger.info("Список заказов пуст или не найден")
        except Exception as e:
            logger.error(f"Ошибка при поиске заказов: {e}")
        try:
            ready_text_element = self.find_element(self.locators.ALL_ORDERS_READY_TEXT)
            if ready_text_element:
                logger.info("Все заказы готовы - заказов в работе нет")
                return None
        except Exception:
            logger.info("Сообщение о готовности заказов не найдено или отсутствует")
        return []

    @allure.step("Проверить отображение списка заказов")
    def is_order_list_displayed(self):
        try:
            return self.element_is_displayed(self.locators.LIST_ORDER)
        except:
            return False

    @allure.step("Ожидать появления списка заказов")
    def wait_for_order_list(self, timeout=20):
        try:
            self.wait_element(self.locators.LIST_ORDER, timeout=timeout)
            return True
        except:
            return False

    @allure.step("Скроллить к списку заказов")
    def scroll_to_order_list(self):
        try:
            self.wait_element(self.locators.IN_PROGRESS_SECTION)
            self.scroll_to_the_element(self.locators.IN_PROGRESS_SECTION)
            logger.info("Скролл к секции 'В работе' выполнен")
        except Exception as e:
            logger.error(f"Не удалось найти секцию 'В работе': {e}")
            self.scroll_to_the_element_by_script(400)
            logger.info("Выполнен скролл на 400px")

    @allure.step("Получить все видимые тексты на странице для отладки")
    def get_all_visible_texts(self):
        try:
            body = self.find_element(BasePageLocators.BODY)
            return body.text
        except:
            return ""

    @allure.step("Кликнуть кнопку 'Конструктор'")
    def click_construct_button(self):
        self.click(BasePageLocators.BUTTON_CONSTRUCT)

    @allure.step("Кликнуть на список заказов")
    def click_order_list(self):
        self.click(BasePageLocators.LENTA_ORDERS)

    @allure.step("Дождаться загрузки страницы заказов")
    def wait_for_orders_page(self):
        self.wait_for_url('/orders')

    @allure.step("Кликнуть кнопку 'Лента заказов'")
    def click_lenta_button(self):
        self.click(self.locators.LENTA_ORDERS)

    @allure.step("Получение количества заказов за сегодня")
    def get_today_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_TO_DAY)
        count_text = self.find_element(LentaPageLocators.COUNT_TO_DAY).text
        return int(count_text)