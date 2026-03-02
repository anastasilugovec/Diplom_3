from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://stellarburgers.example.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def go_to_constructor(self):
        self.driver.find_element(By.XPATH, "//a[text()='Конструктор']").click()

    def go_to_order_list(self):
        self.driver.find_element(By.XPATH, "//a[text()='Лента заказов']").click()