@regressive

Feature: Verify cart shows the correct price

Scenario Outline: Verify cart shows the correct price
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    When user add "<product_name>" to the cart
    Then click on the cart button
    Then user should see "<product_name>" in the cart
    And the item price should show "<price>"
    And click on the hamburger
    And click on the logout button
    And close the browser

    Examples:
    | product_name                      | price  |
    | Sauce Labs Backpack               | $29.99 |
    | Sauce Labs Bike Light             | $9.99  |
    | Sauce Labs Bolt T-Shirt           | $15.99 |
    | Sauce Labs Fleece Jacket          | $49.99 |
    | Sauce Labs Onesie                 | $7.99  |
    | Test.allTheThings() T-Shirt (Red) | $15.99 |