import pytest
from selenium import webdriver
import time



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
    time.sleep(1)
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Countries']").click()
    time.sleep(1)
    # main_window = driver.current_window_handle
    driver.find_element_by_xpath("//table[contains(@class,'dataTable')]//a[text()='Afghanistan']").click()
    driver.find_element_by_xpath("//a[contains(@href,'ISO_3166-1_alpha-2')]").click()
    main_window = driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.switch_to_window(main_window)
    driver.close()
    # driver.find_element_by_xpath("//a[contains(@href,'ISO_3166-1_alpha-3')]").click()
    # driver.switch_to.window(driver.window_handles[1])
    # driver.close()
    # time.sleep(3)
    # driver.find_element_by_xpath("//*[@id='content']/form/table[1]/tbody/tr[6]/td/a").click()
    # # driver.switch_to.window(driver.window_handles[2])
    # time.sleep(3)
