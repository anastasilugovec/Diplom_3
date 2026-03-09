from selenium.webdriver.common.by import By


class LentaPageLocators:
    # Локатор для общего количества заказов за всё время
    COUNT_ALL_TIME = (By.XPATH, "//div[contains(text(), 'Общее количество заказов')]/following-sibling::div")

    # Локатор для количества заказов за сегодня
    COUNT_TO_DAY = (By.XPATH, "//div[contains(text(), 'Заказы сегодня')]/following-sibling::div")

    # Локатор для списка заказов
    LIST_ORDER = (By.CSS_SELECTOR, ".order-card")  # или другой селектор, соответствующий карточкам заказов

    # Локатор для текста "Все заказы готовы"
    ALL_ORDERS_READY_TEXT = (By.XPATH, "//div[contains(text(), 'Все заказы готовы')]")

    # Локатор для секции "В работе" или другой идентификатор секции
    IN_PROGRESS_SECTION = (By.CSS_SELECTOR, ".in-progress-section")  # пример

    # Локатор для тела страницы (для получения всех текстов)
    BODY_ELEMENT = (By.TAG_NAME, "body")