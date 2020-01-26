import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request, browser="ch"):
    if browser == "chrome" or browser == "ch":
        wd = webdriver.Chrome(executable_path=r'Drivers/CH/chromedriver.exe')
        # request.addfinalizer(wd.quit)
    elif browser == "mozilla" or browser == "ff":
        wd = driver = webdriver.Firefox(executable_path=r'Driver/FF/geckodriver.exe')
        # request.addfinalizer(wd.quit)
    else:
        wd = driver = webdriver.Ie(executable_path=r'../Drivers/IE_11/IEDriverServer.exe')
        wd = driver.maximize_window()
        IE_Brows = os.path.dirname(__file__)
        ie_driver_path = IE_Brows + "../Drivers/IE11/IEDriverServer.exe"
        # request.addfinalizer(wd.quit)
    return wd


def test_loading_page(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Appearence']").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Catalog']").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Countries']").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Currencies']").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Customers']").click()
