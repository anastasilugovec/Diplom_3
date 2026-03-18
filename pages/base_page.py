from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получаем нужную страницу")
    def get_urls(self, url):
        self.driver.get(url)

    @allure.step("Получаем атрибут")
    def get_attribute(self, element):
        return self.driver.find_element(*element).get_attribute('value')

    @allure.step("Скроллим до нужного элемента")
    def scroll_to_the_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидание {seconds} секунд")
    def wait_for_time(self, seconds):
        WebDriverWait(self.driver, seconds).until(lambda driver: False)

    @allure.step("Ждем появления элемента")
    def wait_element(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем URL')
    def wait_url(self, url, timeout=15):
        current_url = self.driver.current_url
        print(f"Текущий URL перед ожиданием: {current_url}")
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    def click_to_element(self, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Ищем элемент')
    def find_element(self, element):
        return self.driver.find_element(*element)

    @allure.step('Вводим значение')
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Проверяем что элемент появился на экране')
    def element_is_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    @allure.step("Ждем и находим элемент")
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Проверяем URL')
    def current_url(self, url):
        return self.driver.current_url == url

    @allure.step('Перетаскиваем элемент')
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
        element_obj = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].click();", element_obj)

    @allure.step("Ждем кликабельности элемента")
    def wait_element_clickable(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Ищем элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ждем изменения текста элемента")
    def wait_text_changed(self, locator, initial_text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text != initial_text
        )

    @allure.step("Кликаем по элементу")
    def click(self, locator):
        self.click_to_element(locator)