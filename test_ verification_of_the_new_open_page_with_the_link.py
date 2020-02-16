import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys



@pytest.fixture
def driver(request, browser="ch"):
    if browser == "chrome" or browser == "ch":
        wd = webdriver.Chrome(executable_path=r'Driver/CH/chromedriver.exe')
        # wd = driver.maximize_window()
        request.addfinalizer(wd.quit)
    else:
        wd = webdriver.Firefox(executable_path=r'Driver/FF_026/geckodriver.exe')
        # wd = driver.maximize_window()
        request.addfinalizer(wd.quit)
    return wd


def test_verification_of_the_new_open_page_with_the_link_page(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Countries']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//table[contains(@class,'dataTable')]//a[text()='Afghanistan']").click()
    main_window = driver.current_window_handle
    time.sleep(5)
    first_link = driver.find_element_by_xpath("//a[contains(@href,'ISO_3166-1_alpha-2')]")
    first_link.send_keys(Keys.CONTROL + Keys.RETURN)
    time.sleep(5)
    link = driver.find_element_by_xpath("//body[contains(@class,'mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-ISO_3166-1_alpha-2 rootpage-ISO_3166-1_alpha-2 skin-vector action-view')]")
    link.send_keys(Keys.CONTROL + Keys.TAB)

    # alpha_2 = WebDriverWait(driver, 100).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "page-ISO_3166-1_alpha-2")))
    # alpha_2.send_keys(Keys.CONTROL + Keys.TAB)

    # driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.TAB)
    # driver.switch_to_window(main_window)
