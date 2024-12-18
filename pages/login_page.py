from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class loginPage():
    URL = "https://magento.softwaretestingboard.com/customer/account/login/"

    loginPageMessage = (By.XPATH, "//span[@class='base']")
    loginPageErrorMessage = (By.XPATH, "//div[@class='message-error error message']")

    def __init__(self, driver):
        self.driver = driver

    DASHBOARD_TEXT = ()

    def navigate(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.NAME, "login[password]").send_keys(password)
        self.driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()

    def is_dashboard_displayed(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.loginPageMessage)).text
    
    def error_message(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.loginPageErrorMessage)).text