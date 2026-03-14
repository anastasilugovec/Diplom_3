from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
import allure
import time


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получаем нужную страницу")
    def get_urls(self, element):
        self.driver.get(element)

    @allure.step("Получаем аттрибута")
    def get_attribute(self, element):
        self.get_attribute(element)

    @allure.step("Скролим до нужного элемента")
    def scroll_to_the_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ждем указанное количество секунд')
    def wait(self, seconds=15):
        time.sleep(seconds)

    @allure.step("Ждем появления элемента")
    def wait_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем URL')
    def wait_url(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_contains(url))

    @allure.step("Жмем на элемент")
    def click_to_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Ищем элемент')
    def find_element(self, element):
        return self.driver.find_element(*element)

    @allure.step('Вводим значение')
    def send_keys(self, locator, element):
        self.driver.find_element(*locator).send_keys(element)

    @allure.step('Проверяем что элемент появился на экране')
    def element_is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    @allure.step("Ждем и находим элемент")
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Проверяем URL')
    def current_url(self, locator):
        return self.driver.current_url == locator

    @allure.step('Перетаскиваем эелемент')
    def drag_and_drop(self, source_locator, target_locator):

        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step("Кликаем на элемент через JavaScript")
    def click_to_element_js(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ждем исчезновения элемента")
    def wait_element_invisible(self, locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ждем кликабельности элемента")
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.step('Ищем элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ждем изменения текста элемента")
    def wait_text_changed(self, locator, initial_text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text != initial_text)

    @allure.step("Нажать кнопку 'Конструктор'")
    def click_construct_button(self):
        self.click_to_element_js(BasePageLocators.BUTTON_CONSTRUCT)

    @allure.step("Нажать кнопку 'Лента заказов'")
    def click_lenta_button(self):
        self.click_to_element_js(BasePageLocators.LENTA_ORDERS)

    @allure.step("Нажать кнопку 'Личный кабинет'")
    def click_account_button(self):
        self.click_to_element(BasePageLocators.BUTTON_IN_ACCOUNT)

    @allure.step("Ожидать кликабельности кнопки 'Лента заказов'")
    def wait_lenta_button_clickable(self):
        self.wait_element_clickable(BasePageLocators.LENTA_ORDERS)

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Ожидание указанного количества секунд")
    def wait_for_time(self, seconds):
        time.sleep(seconds)

    @allure.step("Ожидание загрузки конкретного URL")
    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url