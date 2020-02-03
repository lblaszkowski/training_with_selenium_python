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
    for MostPopulars in Most_Popular:

        sticker_name = MostPopulars.find_element_by_xpath("//div[contains(@class,'sticker')]")
        print(sticker_name.text)
        print("--------------")



