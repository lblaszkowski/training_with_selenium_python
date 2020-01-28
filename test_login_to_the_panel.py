import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



@pytest.fixture
def driver(request, browser="ffs"):
    if browser == "chrome" or browser == "ch":
        wd = webdriver.Chrome(executable_path=r'Driver/CH/chromedriver.exe')
        # request.addfinalizer(wd.quit)
    elif browser == "mozilla" or browser == "ff":
        wd = driver = webdriver.Firefox(executable_path=r'Driver/FF/geckodriver.exe')
        # request.addfinalizer(wd.quit)
    elif browser == "mozillas" or browser == "ffs":
        # wd = webdriver.Firefox(capabilities={"marionette": False})
        binary = FirefoxBinary('/path/to/binary')
        driver = webdriver.Firefox(firefox_binary=binary)
    else:
        wd = driver = webdriver.Ie(executable_path=r'Driver/IE11/IEDriverServer.exe')
        IE_Brows = os.path.dirname(__file__)
        ie_driver_path = IE_Brows + "Driver/IE11/IEDriverServer.exe"
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
