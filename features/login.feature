Feature: User Account Management
    As a user, I want to login successfully.

  Scenario: Successful login
    Given user is on the login page
    When user tries to login using valid login credentials
    Then user is logged in successfully

  Scenario: Login with invalid credentials
    Given user is on the login page
    When user tries to login using invalid login credentials
    Then user should see an error message "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."