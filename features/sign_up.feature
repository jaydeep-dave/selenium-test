Feature: User Account Management
    As a user, I want to create an account successfully

  Scenario: Signing up with valid credentials
    Given user is on the account creation page
    When user enters valid registration details
    And user submits registration form
    Then the account is created successfully

  Scenario: Signing up with already used email address
    Given user is on the account creation page
    When user enters already email address and other registration details
    And user submits registration form
    Then user should see an error message in registration page "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."

  Scenario: Signing up with a password which is not fulfilling the requirements
    Given user is on the account creation page
    When user enters a password which is not fulfilling the requirements and other registration details
    And user submits registration form
    Then user should see an error message in registration page for password error "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters."

  Scenario: Signing up with invalid email address
    Given user is on the account creation page
    When user enters invalid email address and other registration details
    And user submits registration form
    Then user should see an error message in registration page for email error "Please enter a valid email address (Ex: johndoe@domain.com)."

  Scenario: Signing up with password and confirmation password not matching
    Given user is on the account creation page
    When user enters different password and confirmation password then other registration details
    And user submits registration form
    Then user should see an error message in registration page for confirmation password error "Please enter the same value again."
