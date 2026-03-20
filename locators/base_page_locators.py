from selenium.webdriver.common.by import By

class BasePageLocators():

    LOGIN_ACCONT = (By.XPATH, ".//p[text()='Личный Кабинет']") #Кнопка перехода "Личный кабинет"

    BUTTON_CONSTRUCT = (By.XPATH, ".//p[text()='Конструктор']") #Кнопка перехода в Конструктор

    LOGO_BURGERS = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип "StarBurgers"

    LENTA_ORDERS = (By.XPATH , ".//p[text()='Лента Заказов']") # Кнопка перехода "Лента заказов"