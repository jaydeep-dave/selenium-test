from behave import given, when, then
from pages.login_page import loginPage

@given("user is on the login page")
def step_impl(context):
    context.page = loginPage(context.driver)
    context.page.navigate()

@when("user tries to login using valid login credentials")
def step_impl(context):
    context.page = loginPage(context.driver)
    context.page.login("abcxyz974@gmail.com", "password@123")

@when("user tries to login using invalid login credentials")
def step_impl(context):
    context.page = loginPage(context.driver)
    context.page.login("abcxyz@gmail.com", "password@123")

@then("user is logged in successfully")
def step_impl(context):
    context.page = loginPage(context.driver)
    homePage_message = context.page.is_dashboard_displayed()
    assert "My Account" in homePage_message, "User not logged in successfully."

@then('user should see an error message "{expected_message}"')
def step_impl(context, expected_message):
    context.page = loginPage(context.driver)
    error_message = context.page.error_message()
    assert error_message == expected_message, f"Expected error message to be '{expected_message}', but got '{error_message}'"