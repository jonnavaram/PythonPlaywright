@regressive
Feature: Remove product from cart

  Scenario: Remove product from cart
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    Then add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    And click on the remove button
    And verify the cart count is decreased or not
    And click on the hamburger
    And click on the logout button
    And close the browser

  
  Scenario: Removed item can be re-added from main page
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    And click on the cart button
    And Verify the product data and cart data same or not
    And click on the remove button
    And click on the continue shopping button
    Then the "Add to cart" button should be visible for "Sauce Labs Backpack"
    And click on the hamburger
    And click on the logout button
    And close the browser









