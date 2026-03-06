from selenium.webdriver.common.by import By


class ProfilePageLocators():
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following::input")  # Поле входа "Email"

    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following::input")  # Поле входа "Пароль"

    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")  # Кнопка входа, в Личном кабинете