@tested

Feature: Customer information at checkout flow

  Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    And click on the cart button
    And click on the checkout button
    Then user should be on the checkout step one page

  Scenario Outline: Proceed with all valid fields
    When user enter first name "<firstname>"
    And user enter last name "<lastname>"
    And user enter postal code "<postalcode"
    And click on the continue button
    And user at overview page
    And the URL should contain "/checkout-step-two.html"
    And click on the hamburger
    And click on the logout button
    And close the browser

    Examples:
    | firstname | lastname |postalcode |
    | sravs | jonnavaram | 123456  |

  Scenario Outline: Submit with empty first name
    And user enter last name "<lastname>"
    And user enter postal code "<postalcode"
    And click on the continue button
    Then user should see the error "First Name is required"
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | lastname |postalcode |
    | jonnavaram | 123456  |

  Scenario Outline: Submit with empty last name
    When user enter first name "<firstname>"
    And user enter postal code "<postalcode"
    And click on the continue button
    Then user should see the error "Last Name is required"
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | firstname | postalcode |
    | sravs     |  123456    |


  Scenario Outline: Submit with empty postal code
    When user enter first name "<firstname>"
    And user enter last name "<lastname>"
    And click on the continue button
    Then user should see the error "Postal Code is required"
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | firstname | lastname |
    | sravs | jonnavaram |


  Scenario: Submit with all fields empty
    And click on the continue button
    Then user should see the error "First Name is required"
    And click on the hamburger
    And click on the logout button
    And close the browser


  Scenario Outline: Error message is dismissable
    And user enter last name "<lastname>"
    And user enter postal code "<postalcode"
    And click on the continue button
    Then user should see the error "First Name is required"
    When user click the error close button
    Then the error message should not be visible
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | lastname |postalcode |
    | jonnavaram | 123456  |



  Scenario: Cancel button returns to cart
    And click on the cancel button
    Then user should be on the cart page
    And the URL should contain "/cart.html"
    And click on the hamburger
    And click on the logout button
    And close the browser


  Scenario Outline: Field accepts valid input formats
    When user enter first name "<first>"
    And user enter last name "<last>"
    And user enter postal code "<postalcode"
    And click on the continue button
    And user at overview page
    And click on the hamburger
    And click on the logout button
    And close the browser


    Examples:
      | first    | last      | zip      |
      | John     | Doe       | 12345    |
      | Mary-Ann | O'Brien   | EC1A 1BB |
      | José     | García    | 560001   |