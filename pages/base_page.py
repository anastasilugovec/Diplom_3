from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def _driver(self):
        return self.driver

    def open(self, url):
        self.driver.get(url)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_element_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_element_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def get_header(self):
        return self.driver.find_element(By.CLASS_NAME, 'Header')

    def click_to_element_js(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_element_disappear(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))

    def click_to_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def drag_and_drop(self, source_locator, target_locator):
        wait = WebDriverWait(self.driver, 15)
        source_element = wait.until(EC.visibility_of_element_located(source_locator))
        target_element = wait.until(EC.visibility_of_element_located(target_locator))
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()