import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request, browser="ff"):
    if browser == "chrome" or browser == "ch":
        wd = webdriver.Chrome(executable_path=r'Driver/CH/chromedriver.exe')
        request.addfinalizer(wd.quit)
    else:
        wd = webdriver.Firefox(executable_path=r'Driver/FF_026/geckodriver.exe')
        request.addfinalizer(wd.quit)
    return wd


def test_adding_to_cart_in_page(driver):
    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li//div[starts-with(@class,'name')]").click()
    options_Size = Select(driver.find_element_by_name("options[Size]"))
    options_Size.select_by_value("Small")
    driver.find_element_by_name("add_cart_product").click()
    time.sleep(1)
    driver.find_element_by_class_name("general-0").click()
    driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li//div[starts-with(@class,'name')]").click()
    options_Size = Select(driver.find_element_by_name("options[Size]"))
    options_Size.select_by_value("Small")
    driver.find_element_by_name("add_cart_product").click()
    time.sleep(1)
    driver.find_element_by_class_name("general-0").click()
    driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li//div[starts-with(@class,'name')]").click()
    options_Size = Select(driver.find_element_by_name("options[Size]"))
    options_Size.select_by_value("Small")
    driver.find_element_by_name("add_cart_product").click()
    time.sleep(1)
    driver.find_element_by_class_name("general-0").click()
    driver.find_element_by_xpath("//a[text()='Checkout »']").click()
    update = driver.find_element_by_name("quantity")
    update.clear()
    update.send_keys("2")
    driver.find_element_by_name("update_cart_item").click()
    time.sleep(1)
    update = driver.find_element_by_name("quantity")
    update.clear()
    update.send_keys("1")
    driver.find_element_by_name("update_cart_item").click()
    time.sleep(1)
    driver.find_element_by_name("remove_cart_item").click()