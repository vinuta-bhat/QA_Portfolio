from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    #ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.XPATH,"//*[@id='shopping_cart_container']/a/span")

    def __init__(self,driver):
        self.driver = driver

    def add_to_cart(self,item_name):
        item_id = item_name.lower().replace(" ","-")
        locator = (By.ID,f"add-to-cart-{item_id}")
        self.driver.find_element(*locator).click()

    def get_shopping_cart_count(self):
        # Add an explicit wait for the badge to become visible
        wait = WebDriverWait(self.driver, 10) # Wait up to 10 seconds
        badge_element = wait.until(EC.visibility_of_element_located(self.SHOPPING_CART_BADGE))
        return badge_element.text