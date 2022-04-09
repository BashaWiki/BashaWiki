Feature: To validate different types of login

  @result @uk @roi @qa
  Scenario: To verify the new user login
    Given The user launched the "Home page"
    And user validates Home page is launched
    When user enters "Username" in Username
    And user enters "Password" in password
    And user click on login button
    Then user should be logged into the page