@tested
Feature: Remove all products from cart

  Scenario: Remove all products from cart
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    Then add all products to the cart
    And click on the cart button
    Then remove all products from the cart
    And cart badge should not be visible
    And click on the hamburger
    And click on the logout button
    And close the browser

