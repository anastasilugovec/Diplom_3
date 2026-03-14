import allure
from locators.lenta_page_locators import LentaPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Lenta(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Получить общее количество заказов за все время")
    def get_all_time_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_ALL_TIME)
        return int(self.find_element(LentaPageLocators.COUNT_ALL_TIME).text)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_TO_DAY)
        return int(self.find_element(LentaPageLocators.COUNT_TO_DAY).text)

    @allure.step("Получить список номеров заказов")
    def get_order_list(self):
        orders = []

        try:
            # Пробуем найти реальные номера заказов (только цифры)
            elements = self.find_elements(LentaPageLocators.LIST_ORDER)
            if elements:
                orders = [order.text for order in elements if order.text.strip() and order.text.strip().isdigit()]
                print(f"Найдено заказов: {len(orders)}")
                return orders
        except Exception as e:
            print(f"Ошибка при поиске заказов: {e}")

        # Если не нашли заказов, проверяем есть ли текст "Все заказы готовы"
        try:
            ready_text_element = self.find_element(LentaPageLocators.ALL_ORDERS_READY_TEXT)
            if ready_text_element:
                print("Все заказы готовы - нет заказов в работе")
                return []
        except:
            print("Нет заказов в работе")

        return orders

    @allure.step("Проверить отображение списка заказов")
    def is_order_list_displayed(self):
        try:
            return self.element_is_displayed(LentaPageLocators.LIST_ORDER)
        except:
            return False

    @allure.step("Ожидать появления списка заказов")
    def wait_for_order_list(self, timeout=20):
        try:
            self.wait_element(LentaPageLocators.LIST_ORDER)
            return True
        except:
            return False

    @allure.step("Скроллить к списку заказов")
    def scroll_to_order_list(self):
        try:
            # Сначала пробуем найти секцию "В работе"
            self.wait_element(LentaPageLocators.IN_PROGRESS_SECTION)
            self.scroll_to_the_element(LentaPageLocators.IN_PROGRESS_SECTION)
            print("Скролл к секции 'В работе' выполнен")
        except Exception as e:
            print(f"Не удалось найти секцию 'В работе': {e}")
            # Скролл вниз страницы
            self.driver.execute_script("window.scrollTo(0, 400);")
            print("Выполнен скролл на 400px")

    @allure.step("Получить все видимые тексты на странице для отладки")
    def get_all_visible_texts(self):
        """Метод для отладки - показывает все тексты на странице"""
        try:
            body = self.find_element((By.TAG_NAME, "body"))
            return body.text
        except:
            return ""