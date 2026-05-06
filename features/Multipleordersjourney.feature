@tested

Feature: Place multiple orders 

  Scenario: Place multiple orders 
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And verify the cart is updated or not
    Then add the "Sauce Labs Bike Light" to cart
    And click on the cart button
    And Verify the multiple products are added in cart or not
    And click on the checkout button
    And enter the information
    And click on the continue button
    And get the payment information and shipping information
    And verify the item total amount
    And add the item total and tax = total bill amount
    And click on the finish button
    And show the order confirmation page
    And click on the hamburger
    And click on the logout button
    And close the browser