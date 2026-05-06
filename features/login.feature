@regressive
Feature: Login functionality

  Scenario: Successful login with standard user
    Given I launch the browser
    When open the home page
    Then verify the title "Swag Labs"
    Then Enter the username and password
    And click on the login button
    Then user should be redirected to the main page
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario Outline: Successful login with performance glitch user
    Given I launch the browser
    When open the home page
    Then verify the title "Swag Labs"
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should be redirected to the main page after a delay
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username | password | 
    | performance_glitch_user  | secret_sauce  | 

  Scenario Outline: Performance glitch user inventory page loads after delay
    Given I launch the browser
    When open the home page
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should be redirected to the main page after a delay
    Then the inventory page should display all 6 products
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username                | password     |
    | performance_glitch_user | secret_sauce |

  Scenario Outline: Successful login with problem user
    Given I launch the browser
    When open the home page
    Then verify the title "Swag Labs"
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should be redirected to the main page
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username |password |
    | problem_user  | secret_sauce |

  Scenario Outline: Successful login with visual user
    Given I launch the browser
    When open the home page
    Then verify the title "Swag Labs"
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should be redirected to the main page
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username    | password     |
    | visual_user | secret_sauce |

  Scenario Outline: Successful login with error user
    Given I launch the browser
    When open the home page
    Then verify the title "Swag Labs"
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should be redirected to the main page
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username   | password     |
    | error_user | secret_sauce |





    

