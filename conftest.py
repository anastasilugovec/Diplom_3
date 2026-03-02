import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver_instance = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == "firefox":
        driver_instance = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()