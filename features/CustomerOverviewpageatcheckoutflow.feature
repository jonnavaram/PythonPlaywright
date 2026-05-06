@regressive

Feature: Checkout step two - order summary

  Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the checkout button
    Then user should be on the checkout step one page
    And user fill the valid checkout information
  
  Scenario: Order summary shows correct item name
    Then user should see "Sauce Labs Backpack" in the order summary
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Order summary shows correct item price
    Then the item price for "Sauce Labs Backpack" should be "$29.99"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Item total is sum of all item prices
    Then the item total should be "$29.99"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Tax is calculated and displayed
    Then the tax amount should be visible and greater than "$0.00"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Grand total equals item total plus tax
    Then the grand total should equal the item total plus tax
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Payment information section is displayed
    Then I should see the payment information section
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Shipping information section is displayed
    Then I should see the shipping information section
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Cancel button returns to main page
    And click on the cancel button
    Then user is in main page
    And the URL should contain "/inventory.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Finish button navigates to order confirmation page
    And click on the finish button
    Then the URL should contain "/checkout-complete.html"
    And click on the back home button
    And click on the hamburger
    And click on the logout button
    And close the browser