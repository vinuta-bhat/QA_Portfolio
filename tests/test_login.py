import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver =webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_unsuccessful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user","wrong_password")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message

def test_login_with_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user1","secret_sauce")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message

def test_login_with_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secretsauce")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message

def test_login_with_blankspace_in_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("       ","secretsauce")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message    

def test_login_with_valid_username_blank_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Password is required" in error_message  

def test_login_with_blank_username_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("","secretsauce")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username is required" in error_message  

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user","secret_sauce")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out." in error_message