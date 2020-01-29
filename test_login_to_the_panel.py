import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



@pytest.fixture
def driver(request, browser="ffn"):
    if browser == "chrome" or browser == "ch":
        wd = webdriver.Chrome(executable_path=r'Driver/CH/chromedriver.exe')
        # request.addfinalizer(wd.quit)
    elif browser == "mozilla" or browser == "ff":
        wd = webdriver.Firefox(executable_path=r'Driver/FF/geckodriver.exe')
        # request.addfinalizer(wd.quit)
    elif browser == "mozillas" or browser == "ffs":
        binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/Firefox_ESR_45/firefox')
        wd = webdriver.Firefox(firefox_binary=binary, capabilities={"marionette": False})
        # request.addfinalizer(wd.quit)
    elif browser == "mozillan" or browser == "ffn":
        binary = FirefoxBinary('C:/Program Files/Firefox Nightly/firefox')
        wd = webdriver.Firefox(firefox_binary=binary)
        # request.addfinalizer(wd.quit)
    else:
        wd = webdriver.Ie(executable_path=r'Driver/IE11/IEDriverServer.exe')
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
