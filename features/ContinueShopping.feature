@regressive
Feature: Continue Shopping button functionality

  Scenario: Continue Shopping from empty cart returns to inventory
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And click on the cart button
    And click on the continue shopping button
    Then user is in main page
    And the URL should contain "/inventory.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Continue Shopping after adding item returns to inventory
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    And click on the cart button
    And click on the continue shopping button
    Then user is in main page
    And the URL should contain "/inventory.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Cart item persists after Continue Shopping and returning to cart
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the continue shopping button
    And user navigate to the cart page again
    Then user should still see "Sauce Labs Backpack" in the cart
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Cart count persists after Continue Shopping
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the continue shopping button
    Then the cart badge should show "1"
    And click on the hamburger
    And click on the logout button
    And close the browser
