@regressive
Feature: Verify Users login

Background: 
    Given I launch the browser
    When open the home page

Scenario Outline: Login with locked user
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then verify the error icon at username
    And verify the error icon at password
    Then user should see the error "Sorry, this user has been locked out."
    And close the browser
    Examples:
        | username|password|
        | locked_out_user  | secret_sauce|

Scenario Outline: Login with incorrect password
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should see an error message containing "Username and password do not match"
    Examples:
        | username|password|
        | standard_user | sauce|

Scenario Outline: Login with incorrect username
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should see an error message containing "Username and password do not match"
    Examples:
    | username|password|
    | stand  | secret_sauce|

Scenario: Login with empty username
    When leave the username field empty
    Then Enter the password "secret_sauce"
    And click on the login button
    Then user should see an error message containing "Username is required"

Scenario Outline: Login with empty password
    Then Enter the username "<username>"
    And leave the password field empty
    And click on the login button
    Then user should see an error message containing "Password is required"
    Examples:
        | username | 
        | standard_user  |   


Scenario Outline: Login with uppercase username (case sensitivity check)
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should see an error message containing "Username and password do not match"
    Examples:
        | username|password|
        | Locked_out_user  | secret_sauce|































