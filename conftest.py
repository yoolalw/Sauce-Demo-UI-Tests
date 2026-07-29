import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)

    yield driver
    driver.quit()
