import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

'''def test_add_inventory(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    cart_count = inventory_page.get_shopping_cart_count()
    assert cart_count == "1" '''

def test_add_inventory_multiple_items(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secret_sauce")

    try:
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='OK']"))
        )
        ok_button.click()
        print("OK button clicked successfully.")
    except TimeoutException:
        print("OK button did not appear within the time limit. Test will continue.")

        
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket"]
    inventory_page = InventoryPage(driver)
    for item in items_to_add:
        inventory_page.add_to_cart(item)
    cart_count = inventory_page.get_shopping_cart_count()
    expected_count = str(len(items_to_add))
    assert cart_count == expected_count
