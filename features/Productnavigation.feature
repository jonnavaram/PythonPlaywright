@regressive

Feature: Verify the product is correctly navigate to detail page

Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And click on the product "Sauce Labs Backpack" 


  Scenario: Verify the product is correctly navigate to detail page
    And verify it navigates to the correct detail page
    And click on the back to products
    Then user is in main page

  Scenario: Add product to cart
    Then click on the add to cart button for "Sauce Labs Backpack"
    Then the cart should be updated as "1"

  Scenario: Navigate the back does not reset the page
      And click on the back to products
      And Verify the full product list is visible

  Scenario: Remove product from the product detail page
    Then click on the add to cart button for "Sauce Labs Backpack"
    Then the cart should be updated as "1"
    Then click on the remove button on the detail page
    Then cart badge should not be visible
    And click on the back to products
    Then user is in main page






    