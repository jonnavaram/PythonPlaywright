@tested
Feature: Empty cart checkout prevention

Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button

Scenario: Checkout with empty cart shows no items on summary
    Then click on the cart button
    And click on the checkout button
    And user fill the valid checkout information
    Then the order summary should show no items
    And the item total should show "$0"
    And click on the hamburger
    And click on the logout button
    And close the browser


Scenario: Empty cart displays appropriate message
    Then the cart item list should be empty
    And "Remove" buttons should not be visible
    And click on the hamburger
    And click on the logout button
    And close the browser