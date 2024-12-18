from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class registrationPage():
    registrationURL = "https://magento.softwaretestingboard.com/customer/account/create/"

    registrationPageMessage = (By.XPATH, "//div[@class='message-success success message']")
    registrationPageErrorMessage = (By.XPATH, "//div[@class='message-error error message']")
    registrationPagePasswordErrorMessage = (By.XPATH, "//div[@id='password-error']")
    registrationPageEmailErrorMessage = (By.XPATH, "//div[@id='email_address-error']")
    registrationPagePasswordConfirmationErrorMessage = (By.XPATH, "//div[@id='password-confirmation-error']")

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.registrationURL)

    def fill_account_form(self, first_name, last_name, email, password, confirmation_password):
        self.driver.find_element(By.ID, "firstname").send_keys(first_name)
        self.driver.find_element(By.ID, "lastname").send_keys(last_name)
        self.driver.find_element(By.ID, "email_address").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "password-confirmation").send_keys(confirmation_password)

    def submit_form(self):
        self.driver.find_element(By.XPATH, "//button[@title='Create an Account']").click()

    def  verify_if_registration_successfully(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.registrationPageMessage)).text
    
    def error_message(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.registrationPageErrorMessage)).text
    
    def email_error_message(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.registrationPageEmailErrorMessage)).text
    
    def password_error_message(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.registrationPagePasswordErrorMessage)).text
    
    def password_confirmation_error_message(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.registrationPagePasswordConfirmationErrorMessage)).text