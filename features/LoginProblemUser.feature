@regressive

Feature: Login with problem user and verify

Scenario Outline: Problem user sees broken or different product images
    Given I launch the browser
    When open the home page
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    When click on the product "<product_name>"
    Then the product image should be broken or different
    And close the browser
    Examples:
        | username     | password     | product_name        |
        | problem_user | secret_sauce | Sauce Labs Backpack |


Scenario Outline: Problem user can login successfully
    Given I launch the browser
    When open the home page
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user is in main page
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
        | username     | password     |
        | problem_user | secret_sauce |


Scenario: Problem user is unable to complete checkout due to form validation bug
    Given I launch the browser
    When open the home page
    Then Enter the username "problem_user"
    Then Enter the password "secret_sauce"
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the checkout button
    Then user should be on the checkout step one page
    When user enter first name "Test"
    And user enter last name "User"
    And user enter postal code "12345"
    And click on the continue button
    Then user should see the error "Last Name is required"
    And close the browser


