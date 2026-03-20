import requests
import allure

class AuthAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    @allure.step("Логин пользователя с email: {email}")
    def login(self, email, password):
        url = f"{self.base_url}/api/auth/login"
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            self.token = response.json().get("accessToken")
            print("Успешный вход. Токен:", self.token)
        else:
            raise Exception(f"Ошибка входа: {response.status_code} - {response.text}")