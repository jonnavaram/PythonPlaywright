@tested

Feature: Order confirmation page

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
    And click on the finish button

  Scenario: Thank you message is displayed on confirmation page
    Then I should see the "THANK YOU FOR YOUR ORDER!" heading
    And click on the back home button
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Order dispatched message is displayed
    Then I should see the order dispatched confirmation text
    And click on the back home button
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Confirmation page URL is correct
    Then the URL should contain "/checkout-complete.html"
    And click on the back home button
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Back Home button returns to inventory
    And click on the back home button
    Then user is in main page
    And the URL should contain "/inventory.html"
    And click on the hamburger
    And click on the logout button
    And close the browser
