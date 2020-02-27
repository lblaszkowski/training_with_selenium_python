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
    price_name = driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li//s[starts-with(@class,'regular-price')]").text
    print(price_name)
    price_name_color = driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//s").value_of_css_property("color")
    print(price_name_color)
    price_promotion_name = driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li//strong[starts-with(@class,'campaign-price')]").text
    driver.execute_script("window.scrollTo(0, 500)")
    product = driver.find_element_by_xpath("//div[contains(@id,'box-campaigns')]//ul[contains(@class,'listing-wrapper')]//li")
    product.click()
    verification_name_product = driver.find_element_by_xpath("//div[contains(@class,'content')]//h1[contains(@class,'title')]").text
    verification_price_name = driver.find_element_by_xpath("//div[contains(@class,'content')]//s[contains(@class,'regular-price')]").text
    verification_price_promotion_name = driver.find_element_by_xpath("//div[contains(@class,'content')]//strong[contains(@class,'campaign-price')]").text


    assert (name_product == verification_name_product), f"{name_product} ':' {verification_name_product} - nazwy produktów są różne"
    assert (price_name == verification_price_name), f"{price_name} ':' {verification_price_name} - kwoty podstawowe są różne"
    assert (price_promotion_name == verification_price_promotion_name), f"{price_promotion_name} ':' {verification_price_promotion_name} - kwoty promocyjne są różne"
    #
