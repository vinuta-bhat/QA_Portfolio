from selenium.webdriver.common.by import By

class InventoryPage:
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.XPATH,"//*[@id='shopping_cart_container']/a/span")

    def __init__(self,driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def get_shopping_cart_count(self):
        return self.driver.find_element(*self.SHOPPING_CART_BADGE).text