from selenium.webdriver.common.by import By


class LentaPageLocators():
    COUNT_ALL_TIME = (By.XPATH,
                      './/div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')  # Количество заказов за все время

    COUNT_TO_DAY = (By.XPATH,
                    "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")  # Количество заказов за сегодня

    LIST_ORDER = (By.XPATH,
                  "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]")  # Список заказов в работе

    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")
    ORDER_NUMBERS = (By.CLASS_NAME, "text_type_digits-default")
    ORDER_FEED = (By.CLASS_NAME, "OrderFeed_orderListReady")
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе')]")
    LENTA_ORDERS = (By.XPATH, ".//p[text()='Лента Заказов']")
    ALL_ORDERS_READY_TEXT = (By.XPATH, "//div[contains(text(), 'Все заказы готовы')]")
    BODY = (By.TAG_NAME, "body")
    LENTA_BUTTON = (By.XPATH, "//button[@class='lenta-button']")
    LENTA_ORDERS = (By.XPATH, ".//p[text()='Лента Заказов']")