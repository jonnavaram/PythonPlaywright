@regressive

Feature: Hamburger menu navigation and functionality

  Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button

  Scenario: All Items link navigates back to inventory from cart page
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the hamburger
    And click on the All Items link
    Then user is in main page
    And the URL should contain "/inventory.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: About link navigates to external SauceLabs page
    And click on the hamburger
    And click on the About link
    Then the URL should contain "saucelabs.com"
    And close the browser

  Scenario: Reset App State clears cart items
    And add all products to the cart
    And click on the hamburger
    And click on the Reset App State link
    Then cart badge should not be visible
    And click on the logout button
    And close the browser

  Scenario: Reset App State resets Add to Cart buttons
    And add the "Sauce Labs Backpack" to cart
    And click on the hamburger
    And click on the Reset App State link
    Then the "Add to cart" button should not be visible for "Sauce Labs Backpack"
    And click on the logout button
    And close the browser
