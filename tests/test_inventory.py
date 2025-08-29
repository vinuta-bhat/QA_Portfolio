import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_inventory(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    cart_count = inventory_page.get_shopping_cart_count()
    assert cart_count == "1"
