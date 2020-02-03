import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request, browser="ff"):
    if browser == "chrome" or browser == "ch":
        wd = webdriver.Chrome(executable_path=r'Driver/CH/chromedriver.exe')
        print("starts chrome")
        request.addfinalizer(wd.quit)
    else:
        wd = webdriver.Firefox(executable_path=r'Driver/FF_026/geckodriver.exe')
        print("starts mozilla")
        request.addfinalizer(wd.quit)
    return wd



def test_loading_page(driver):
    driver.get("http://localhost/litecart/")
    Most_Popular = driver.find_elements_by_xpath("//div[contains(@id,'box-most-popular')]//ul[contains(@class,'listing-wrapper')]//li")
    MostPopular_count = len(Most_Popular)
    # sticker_name = driver.find_elements_by_xpath(".//div[contains(@class,'sticker')]")
    sticker_name = driver.find_elements_by_xpath("//div[contains(@id,'box-most-popular')]//ul[contains(@class,'listing-wrapper')]//li//div[contains(@class,'sticker')]")
    number_of_stickers = len(sticker_name)
    assert (MostPopular_count == number_of_stickers), f"{MostPopular_count} ':' {number_of_stickers} - is not equal to the number of product stickers"

