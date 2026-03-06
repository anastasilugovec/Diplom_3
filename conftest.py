import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from faker import Faker
from urls import Urls  # Импортируем класс Urls из вашего существующего файла


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            service = Service(ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'."
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def urls():
    return Urls()


@pytest.fixture
def login_user(urls):
    fake = Faker(locale="ru_RU")

    payload = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

    requests.post(f'{urls.STELLAR_BURGER_CONSTRUCT}/api/auth/register', data=payload)

    login_response = requests.post(f"{urls.STELLAR_BURGER_CONSTRUCT}/api/auth/login", data={
        "email": payload["email"],
        "password": payload["password"]
    })

    access_token = login_response.json()["accessToken"]

    user_data = {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "accessToken": access_token
    }

    yield user_data

    headers = {"Authorization": f"Bearer {access_token}"}
    requests.delete(f"{urls.STELLAR_BURGER_CONSTRUCT}/api/auth/user", headers=headers)