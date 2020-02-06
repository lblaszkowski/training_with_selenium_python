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
    driver.find_element_by_xpath("//a[text()='New customers click here']").click()
    tax_id = driver.find_element_by_name("tax_id")
    tax_id.send_keys("")
    company = driver.find_element_by_name("company")
    company.send_keys("Polska")
    firstname = driver.find_element_by_name("firstname")
    firstname.send_keys("marcelina")
    lastname = driver.find_element_by_name("lastname")
    lastname.send_keys("kos")
    address1 = driver.find_element_by_name("address1")
    address1.send_keys("Jana Nowaka")
    postcode = driver.find_element_by_name("postcode")
    postcode.send_keys("80-627")
    city = driver.find_element_by_name("city")
    city.send_keys("Gdańsk")
    email = driver.find_element_by_name("email")
    email.send_keys("marcelina.kos111@we.pl")
    phone = driver.find_element_by_name("phone")
    phone.send_keys("123456789")
    password = driver.find_element_by_name("password")
    password.send_keys("Legia09aa")
    confirmed_password = driver.find_element_by_name("confirmed_password")
    confirmed_password.send_keys("Legia09aa")
    driver.find_element_by_name("create_account").click()
    Logout_klick = driver.find_element_by_xpath("//div[contains(@class,'content')]//ul[contains(@class,'list-vertical')]//a[text()='Logout']")
    Logout_klick.click()
    email = driver.find_element_by_name("email")
    email.send_keys("marcelina.kos@interia.pl")
    password = driver.find_element_by_name("password")
    password.send_keys("Legia09aa")
    driver.find_element_by_name("login").click()
    Logout_klick = driver.find_element_by_xpath("//div[contains(@class,'content')]//ul[contains(@class,'list-vertical')]//a[text()='Logout']")
    Logout_klick.click()





