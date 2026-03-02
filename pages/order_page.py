from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def create_order(self):
        self.driver.find_element(By.XPATH, "//button[text()='Создать заказ']").click()

    def get_total_completed_count(self):
        count = self.driver.find_element(By.XPATH, "//div[text()='Выполнено за всё время']/following-sibling::div")
        return int(count.text)

    def get_today_completed_count(self):
        count = self.driver.find_element(By.XPATH, "//div[text()='Выполнено за сегодня']/following-sibling::div")
        return int(count.text)

    def get_current_order_number(self):
        return self.driver.find_element(By.CLASS_NAME, 'OrderNumber').text

    def is_order_in_work(self, order_number):
        orders = self.driver.find_elements(By.CLASS_NAME, 'OrderInWork')
        return any(order.text == order_number for order in orders)