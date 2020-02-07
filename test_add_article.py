import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request, browser="ff"):
    if browser == "chrome" or browser == "ch":
        wd = webdriver.Chrome(executable_path=r'Driver/CH/chromedriver.exe')
        # wd = driver.maximize_window()
        request.addfinalizer(wd.quit)
    else:
        wd = webdriver.Firefox(executable_path=r'Driver/FF_026/geckodriver.exe')
        # wd = driver.maximize_window()
        request.addfinalizer(wd.quit)
    return wd


def test_loading_page(driver, name_file='Kaczkaasas'):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Catalog']").click()
    driver.find_element_by_xpath("//*[@id='content']/div[1]/a[2]/i").click()
    driver.find_element_by_name("name[en]").send_keys(name_file)
    driver.find_element_by_name("code").send_keys("123")
    driver.find_element_by_name("categories[]").click()
    if driver.find_element_by_xpath("//*[@id='tab-general']/table/tbody/tr[4]/td/div/table/tbody/tr[2]/td[1]/input").is_displayed():
        driver.find_element_by_xpath("//*[@id='tab-general']/table/tbody/tr[4]/td/div/table/tbody/tr[2]/td[1]/input").click()
    driver.find_element_by_name("product_groups[]").click()
    quantity = driver.find_element_by_name("quantity")
    quantity.click()
    quantity.send_keys("10")
    quantity_unit_id = Select(driver.find_element_by_name("quantity_unit_id"))
    quantity_unit_id.select_by_value("1")
    delivery_status_id = Select(driver.find_element_by_name("delivery_status_id"))
    delivery_status_id.select_by_value("1")
    sold_out_status_id = Select(driver.find_element_by_name("sold_out_status_id"))
    sold_out_status_id.select_by_value("1")
    driver.find_element_by_name("date_valid_from").click()
    driver.find_element_by_name("date_valid_to").click()
    driver.find_element_by_name("save").click()
    name_file_product = driver.find_element_by_xpath("//tr[contains(@class,'row')]//a[text()='" + name_file + "']")
    assert (name_file_product.text == name_file), f"{name_file_product} ':' {name_file} - stworzona nazwa produktu jest różna"
