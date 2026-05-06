@tested
Feature: Checkout form field validation

  Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the checkout button

  Scenario: Submit with empty first name shows error
    And leave the last name and postal code filled but first name empty
    And click on the continue button
    Then user should see a checkout error message containing "First Name is required"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Submit with empty last name shows error
    And leave the first name and postal code filled but last name empty
    And click on the continue button
    Then user should see a checkout error message containing "Last Name is required"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Submit with empty postal code shows error
    And leave the first name and last name filled but postal code empty
    And click on the continue button
    Then user should see a checkout error message containing "Postal Code is required"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Submit with all fields empty shows first name error
    And click on the continue button
    Then user should see a checkout error message containing "First Name is required"
    And click on the hamburger
    And click on the logout button
    And close the browser

  Scenario: Dismiss checkout error message
    And click on the continue button
    Then user should see a checkout error message containing "First Name is required"
    And dismiss the checkout error message
    Then the checkout error message should not be visible
    And click on the hamburger
    And click on the logout button
    And close the browser
