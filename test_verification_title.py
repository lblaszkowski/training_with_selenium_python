import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request, browser="ffn"):
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
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Appearence']").click()

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Template']").click()
    verification = driver.find_element_by_xpath("//td[contains(@id,'content')]")
    verification_Template = verification.find_element_by_xpath("//h1[text()=' Template']")
    assert verification_Template.text == "Template"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Logotype']").click()
    verification_Logotype = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Logotype']")
    assert verification_Logotype.text == "Logotype"
