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



def test_loading_page(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Catalog']").click()
    driver.find_element_by_xpath("//*[@id='content']/div[1]/a[1]/i").click()
    driver.find_element_by_name("name[en]").send_keys("Kaczka")
    driver.find_element_by_name("code").send_keys("1234")
    Parent_Category = Select(driver.find_element_by_name("parent_id"))
    Parent_Category.select_by_value("1")
    driver.find_element_by_name("google_taxonomy_id")
    driver.find_element_by_name("dock[]")
    List_Style = Select(driver.find_element_by_name("list_style"))
    List_Style.select_by_value("rows")
    driver.find_element_by_name("keywords")
    add_image = driver.find_element_by_name("image")
    add_image.click()
    add_image.send_keys("C:/training_with_selenium_python/image/rodzinnespotkania.jpeg")
    driver.find_element_by_name("priority").send_keys("123")
    driver.find_element_by_xpath("//div[contains(@id,'content-wrapper')]//a[text()='Information']").click()
    driver.find_element_by_name("h1_title[en]").send_keys("Kaczka")
    driver.find_element_by_name("short_description[en]").send_keys("Opis -- Kaczka")


