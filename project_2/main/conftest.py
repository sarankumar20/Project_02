from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from project_2.SRC.data import Value


@pytest.fixture()
def start_and_quit(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Value.homepage_url)
    request.cls.driver = driver
    yield
    driver.quit()