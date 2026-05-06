@regressive
Feature: Download the product image

  Scenario: Download the product image
    Given I launch the browser
    When open the home page
    Then verify the title "Swag Labs"
    Then Enter the username and password
    And click on the login button
    And click on the "Sauce Labs Backpack" image
    Then download the image

  Scenario Outline: Download image for each product
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    And click on the "<product_name>" image
    Then download the image

    Examples:
    | product_name                      |
    | Sauce Labs Bike Light             |
    | Sauce Labs Bolt T-Shirt           |
    | Sauce Labs Fleece Jacket          |
    | Sauce Labs Onesie                 |
    | Test.allTheThings() T-Shirt (Red) |

