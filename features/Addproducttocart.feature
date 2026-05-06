@tested

Feature: Add product to cart

  Scenario: Add product to cart
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Cart badge shows correct count when multiple products are added
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    Then add all products to the cart
    Then the cart badge should show "6"
    And click on the hamburger
    And click on the logout button
    And close the browser
