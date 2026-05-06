@tested

Feature: Unable to place the order from Error user

 Scenario Outline: Unable to place the order from Error user
    Given I launch the browser
    When open the home page
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    And click on the cart button
    And Verify the product data and cart data same or not
    And click on the checkout button
    And enter the information
    And click on the continue button
    And get the payment information and shipping information
    And verify the item total amount
    And add the item total and tax = total bill amount
    And unable to click on the finish button
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
        | username| password|
        | error_user  | secret_sauce |

