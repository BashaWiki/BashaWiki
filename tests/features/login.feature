@testing
Feature: To validate different types of login

  @testing
  Scenario: To verify the user login
    Given The user launched the "Google"
    And user validates Home page is launched
    When user enters "Username" in Username
    And user enters "Password" in password
    And user click on login button
    Then user should be logged into the page