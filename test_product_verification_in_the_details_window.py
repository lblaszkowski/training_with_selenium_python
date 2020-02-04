import pytest
from selenium import webdriver
import time

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



def test_loading_page(driver):
    driver.get("http://localhost/litecart/")
    name_product = driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li//div[starts-with(@class,'name')]").text
    print(name_product)
    price_name = driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li//strong[starts-with(@class,'campaign-price')]").text
    print(price_name)
    driver.execute_script("window.scrollTo(0, 500)")
    product = driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li")
    product.click
    time.sleep(5)