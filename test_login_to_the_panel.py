import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = driver = webdriver.Firefox(executable_path=r'../training_with_selenium_python/geckodriver.exe')
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
