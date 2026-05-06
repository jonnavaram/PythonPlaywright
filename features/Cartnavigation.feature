@regressive

Feature: Cart navigation and state management

Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    
Scenario: Cart icon navigates to cart page
    Then click on the cart button
    Then user should be on the cart page
    And the URL should contain "/cart.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

Scenario: Continue Shopping returns to main page
    Then click on the cart button
    And click on the continue shopping button
    Then user is in main page
    And click on the hamburger
    And click on the logout button
    And close the browser

Scenario: Cart state is preserved after continuing shopping
    And add the "Sauce Labs Backpack" to cart
    Then click on the cart button
    And click on the continue shopping button
    And user navigate to the cart page again
    Then user should still see "Sauce Labs Backpack" in the cart
    And click on the hamburger
    And click on the logout button
    And close the browser


  Scenario: Checkout button navigates to checkout step one
    And add the "Sauce Labs Backpack" to cart
    Then click on the cart button
    And click on the checkout button
    Then user should be on the checkout step one page
    And the URL should contain "/checkout-step-one.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Cart badge is not visible when cart is empty on login
    Then cart badge should not be visible
    And click on the hamburger
    And click on the logout button
    And close the browser


