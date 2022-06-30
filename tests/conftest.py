import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROME_DRIVER_PATH = 'chromedriver.exe'
URL = 'https://www.saucedemo.com/'


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximize')
    options.add_argument('--window-size=800,600')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(
        executable_path=CHROME_DRIVER_PATH,
        options=options
    )
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = URL
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
