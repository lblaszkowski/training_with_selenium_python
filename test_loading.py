import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = driver = webdriver.Firefox(executable_path=r'Driver/FF/geckodriver.exe')
    request.addfinalizer(wd.quit)
    return wd



def test_loading_page(driver):
    driver.get("https://www.google.com")
    driver.close()
    driver.quit()