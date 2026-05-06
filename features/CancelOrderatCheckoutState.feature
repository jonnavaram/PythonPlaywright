@tested
Feature: Cancel the order at checkout state

  Scenario: Cancel the order at checkout state
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    And click on the cart button
    And Verify the product data and cart data same or not
    And click on the checkout button
    And click on the cancel button
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Cancel the order at checkout overview page returns to inventory
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    And click on the cart button
    And click on the checkout button
    And user fill the valid checkout information
    And click on the cancel button
    Then user is in main page
    And the URL should contain "/inventory.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Cancel at checkout step one returns to cart page
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the checkout button
    Then user should be on the checkout step one page
    And click on the cancel button
    Then user should be on the cart page
    And the URL should contain "/cart.html"
    And click on the hamburger
    And click on the logout button
    And close the browser