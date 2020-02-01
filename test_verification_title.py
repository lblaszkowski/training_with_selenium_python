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



    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Catalog']").click()
    verification_Catalog = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Catalog']")
    assert verification_Catalog.text == "Catalog"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Product Groups']").click()
    verification_Product_Groups = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Product Groups']")
    assert verification_Product_Groups.text == "Product Groups"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Manufacturers']").click()
    verification_Manufacturers = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Manufacturers']")
    assert verification_Manufacturers.text == "Manufacturers"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Suppliers']").click()
    verification_Suppliers = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Suppliers']")
    assert verification_Suppliers.text == "Suppliers"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Delivery Statuses']").click()
    verification_Delivery_Statuses = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Delivery Statuses']")
    assert verification_Delivery_Statuses.text == "Delivery Statuses"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Sold Out Statuses']").click()
    verification_Sold_Out_Statuses = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Sold Out Statuses']")
    assert verification_Sold_Out_Statuses.text == "Sold Out Statuses"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Quantity Units']").click()
    verification_Quantity_Units = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Quantity Units']")
    assert verification_Quantity_Units.text == "Quantity Units"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='CSV Import/Export']").click()
    verification_CSV_ImportExport = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' CSV Import/Export']")
    assert verification_CSV_ImportExport.text == "CSV Import/Export"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Countries']").click()
    verification_Countries = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Countries']")
    assert verification_Countries.text == "Countries"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Currencies']").click()
    verification_Currencies = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Currencies']")
    assert verification_Currencies.text == "Currencies"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Customers']").click()
    verification_Customers = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Customers']")
    assert verification_Customers.text == "Customers"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='CSV Import/Export']").click()
    verification_CSV_ImportExport = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' CSV Import/Export']")
    assert verification_CSV_ImportExport.text == "CSV Import/Export"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Newsletter']").click()
    verification_Newsletter = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Newsletter']")
    assert verification_Newsletter.text == "Newsletter"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Geo Zones']").click()
    verification_Geo_Zones = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Geo Zones']")
    assert verification_Geo_Zones.text == "Geo Zones"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Languages']").click()
    verification_Languages = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Languages']")
    assert verification_Languages.text == "Languages"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Storage Encoding']").click()
    verification_Storage_Encoding = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Storage Encoding']")
    assert verification_Storage_Encoding.text == "Storage Encoding"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Modules']").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Background Jobs']").click()
    verification_Background_Jobs = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Job Modules']")
    assert verification_Background_Jobs.text == "Job Modules"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Customer']").click()
    verification_Customer = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Customer Modules']")
    assert verification_Customer.text == "Customer Modules"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Shipping']").click()
    verification_Shipping_Modules = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Shipping Modules']")
    assert verification_Shipping_Modules.text == "Shipping Modules"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Payment']").click()
    verification_Payment_Modules  = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Payment Modules']")
    assert verification_Payment_Modules.text == "Payment Modules"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Order Total']").click()
    verification_Order_Total_Modules = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Order Total Modules']")
    assert verification_Order_Total_Modules.text == "Order Total Modules"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Order Success']").click()
    verification_Order_Success = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Order Success Modules']")
    assert verification_Order_Success.text == "Order Success Modules"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Order Action']").click()
    verification_Order_Action_Modules = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Order Action Modules']")
    assert verification_Order_Action_Modules.text == "Order Action Modules"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Orders']").click()
    verification_Orders = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Orders']")
    assert verification_Orders.text == "Orders"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Order Statuses']").click()
    verification_Order_Status = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Order Statuses']")
    assert verification_Order_Status.text == "Order Statuses"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Pages']").click()
    verification_Pages = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Pages']")
    assert verification_Pages.text == "Pages"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Reports']").click()
    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Monthly Sales']").click()
    verification_Monthly_Sales = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Monthly Sales']")
    assert verification_Monthly_Sales.text == "Monthly Sales"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Most Sold Products']").click()
    verification_Most_Sold_Products = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Most Sold Products']")
    assert verification_Most_Sold_Products.text == "Most Sold Products"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Most Shopping Customers']").click()
    verification_Most_Shopping_Customers = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Most Shopping Customers']")
    assert verification_Most_Shopping_Customers.text == "Most Shopping Customers"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Settings']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Defaults']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='General']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Listings']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Images']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Checkout']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Advanced']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Security']").click()
    verification_Settings = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Settings']")
    assert verification_Settings.text == "Settings"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Slides']").click()
    verification_Slides = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Slides']")
    assert verification_Slides.text == "Slides"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Tax']").click()
    verification_Tax_Classes = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Tax Classes']")
    assert verification_Tax_Classes.text == "Tax Classes"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Tax Rates']").click()
    verification_Tax_Rates = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Tax Rates']")
    assert verification_Tax_Rates.text == "Tax Rates"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Translations']").click()
    verification_Search_Translations = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Search Translations']")
    assert verification_Search_Translations.text == "Search Translations"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Scan Files']").click()
    verification_Scan_Files_For_Translations = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Scan Files For Translations']")
    assert verification_Scan_Files_For_Translations.text == "Scan Files For Translations"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='CSV Import/Export']").click()
    verification_CSV_ImportExport = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' CSV Import/Export']")
    assert verification_CSV_ImportExport.text == "CSV Import/Export"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='Users']").click()
    verification_CSV_ImportExport = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' Users']")
    assert verification_CSV_ImportExport.text == "Users"

    driver.find_element_by_xpath("//li[contains(@id,'app')]//span[text()='vQmods']").click()
    verification_CSV_ImportExport = driver.find_element_by_xpath("//td[contains(@id,'content')]//h1[text()=' vQmods']")
    assert verification_CSV_ImportExport.text == "vQmods"