from selenium.webdriver.common.by import By


class ConstructPageLocators:
    TEXT_BURGER_CONSTRUCT = [By.XPATH,
                             ".//h1[text()='Соберите бургер']"]  # Текст "Соберите бургер", на странице Конструктора

    BUNS_PAGE = (By.XPATH, ".//span[text()='Булки']/parent::div")  # Раздел булок в ингредиентах

    BUN_INGRIDIENT = [By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]']  # Булка в разделе булок

    BUN_COUNTER = (By.XPATH,
                   ".//p[text()='Флюоресцентная булка R2-D3']/../div/p[@class='counter_counter__num__3nue1']")  # Счетчик булок

    TOPPINGS_PAGE = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # Раздел начинки в ингредиентах

    TOPPING_INGRIDIENT = (By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]')  # Начинка в разделе начинок

    WINDOW_INGRIDIENT = (By.XPATH, ".//h2[text()='Детали ингредиента']")  # Окно ингредиента

    WINDOW_CROSS = (By.XPATH,
                    ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div/button")  # Кнопка закрытия окна ингредиента

    BURGER_ORDER_LIST = (By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]')  # Список ингредиентов заказа

    BUTTON_IN_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка перехода "Войти в аккаунт"

    BUTTON_ORDER = (By.XPATH,
                    './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')  # Кнопка заказать

    NUMBER_ORDER = (By.XPATH,
                    './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')  # Номер заказа

    CLOSE_BUTTON_ORDER_WINDOW = (By.XPATH,
                                 './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')  # Кнопка закрытия окна заказа