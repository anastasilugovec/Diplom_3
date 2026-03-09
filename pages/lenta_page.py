import allure
from locators.lenta_page_locators import LentaPageLocators
from pages.base_page import BasePage

class Lenta(BasePage):

    @allure.step("Получить общее количество заказов за все время")
    def get_all_time_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_ALL_TIME)
        return int(self.find_element(LentaPageLocators.COUNT_ALL_TIME).text)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_TO_DAY)
        return int(self.find_element(LentaPageLocators.COUNT_TO_DAY).text)

    @allure.step("Проверить наличие текста 'Все заказы готовы'")
    def is_all_orders_ready_text_present(self):
        try:
            element = self.find_element(LentaPageLocators.ALL_ORDERS_READY_TEXT)
            return element.is_displayed()
        except:
            return False

    @allure.step("Получить список номеров заказов")
    def get_order_list(self):
        orders = []

        try:
            # Ищем карточки заказов
            elements = self.find_elements(LentaPageLocators.LIST_ORDER)
            if elements:
                # Отфильтровываем только цифровые номера заказов
                orders = [order.text for order in elements if order.text.strip() and order.text.strip().isdigit()]
                return orders
        except:
            pass

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
            self.wait_element(LentaPageLocators.LIST_ORDER, timeout=timeout)
            return True
        except:
            return False

    @allure.step("Скроллить к секции 'В работе'")
    def scroll_to_in_progress_section(self):
        try:
            if self.element_is_displayed(LentaPageLocators.IN_PROGRESS_SECTION):
                self.scroll_to_the_element(LentaPageLocators.IN_PROGRESS_SECTION)
            else:
                self.driver.execute_script("window.scrollTo(0, 400);")
        except:
            self.driver.execute_script("window.scrollTo(0, 400);")

    @allure.step("Получить все видимые тексты на странице")
    def get_all_visible_texts(self):
        try:
            body = self.find_element(LentaPageLocators.BODY_ELEMENT)
            return body.text
        except:
            return ""