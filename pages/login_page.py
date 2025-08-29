from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID,"user-name")
    PASSWORD_FIELD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR,'h3[data-test="error"]')

    def __init__(self,driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self,username,password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    # A method to get the text of an error message.
    
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text