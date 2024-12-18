from behave import given, when, then
from utility import utils
from pages.sign_up_page import registrationPage

@given("user is on the account creation page")
def step_impl(context):
    context.page = registrationPage(context.driver)
    context.page.navigate()

@when("user enters valid registration details")
def step_impl(context):
    context.page = registrationPage(context.driver)
    context.page.fill_account_form("firstName", "lastName", utils.generate_random_email(), "Password@123", "Password@123")

@when("user enters already email address and other registration details")
def step_impl(context):
    context.page = registrationPage(context.driver)
    context.page.fill_account_form("Abc", "Xyz", "abcxyz974@gmail.com", "Password@123", "Password@123")

@when("user enters a password which is not fulfilling the requirements and other registration details")
def step_impl(context):
    context.page = registrationPage(context.driver)
    context.page.fill_account_form("firstName", "lastName", utils.generate_random_email(), "password", "password")

@when("user enters invalid email address and other registration details")
def step_impl(context):
    context.page = registrationPage(context.driver)
    context.page.fill_account_form("firstName", "lastName", 'abcxyz', "Password@123", "Password@123")

@when("user enters different password and confirmation password then other registration details")
def step_impl(context):
    context.page = registrationPage(context.driver)
    context.page.fill_account_form("firstName", "lastName", utils.generate_random_email(), "Password@123", "Password")

@when("user submits registration form")
def step_impl(context):
    context.page = registrationPage(context.driver)
    context.page.submit_form()

@then("the account is created successfully")
def step_impl(context):
    context.page = registrationPage(context.driver)
    confirmation_message = context.page.verify_if_registration_successfully()
    assert "Thank you for registering with Main Website Store." in confirmation_message, "Registration is not successful."
    
@then('user should see an error message in registration page "{expected_message}"')
def step_impl(context, expected_message):
    context.page = registrationPage(context.driver)
    error_message = context.page.error_message()
    assert error_message == expected_message, f"Expected error message to be '{expected_message}', but got '{error_message}'"

@then('user should see an error message in registration page for password error "{expected_message}"')
def step_impl(context, expected_message):
    context.page = registrationPage(context.driver)
    error_message = context.page.password_error_message()
    assert error_message == expected_message, f"Expected error message to be '{expected_message}', but got '{error_message}'"

@then('user should see an error message in registration page for email error "{expected_message}"')
def step_impl(context, expected_message):
    context.page = registrationPage(context.driver)
    error_message = context.page.email_error_message()
    assert error_message == expected_message, f"Expected error message to be '{expected_message}', but got '{error_message}'"

@then('user should see an error message in registration page for confirmation password error "{expected_message}"')
def step_impl(context, expected_message):
    context.page = registrationPage(context.driver)
    error_message = context.page.password_confirmation_error_message()
    assert error_message == expected_message, f"Expected error message to be '{expected_message}', but got '{error_message}'"