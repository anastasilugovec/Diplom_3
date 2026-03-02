from selenium.webdriver.common.by import By

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver

    def open_ingredient_details(self, ingredient_name):
        ingredient = self.driver.find_element(By.XPATH, f"//div[text()='{ingredient_name}']")
        ingredient.click()

    def is_modal_open(self):
        return self.driver.find_element(By.CLASS_NAME, 'IngredientDetails_modal').is_displayed()

    def close_modal(self):
        self.driver.find_element(By.CLASS_NAME, 'CloseButton').click()

    def add_ingredient_to_order(self, ingredient_name):
        ingredient = self.driver.find_element(By.XPATH, f"//div[text()='{ingredient_name}']")
        ingredient.click()
        self.driver.find_element(By.XPATH, "//button[text()='Добавить в заказ']").click()

    def get_ingredient_counter(self, ingredient_name):
        counter_element = self.driver.find_element(By.XPATH, f"//div[text()='{ingredient_name}']/following-sibling::div[@class='Counter']")
        return int(counter_element.text)