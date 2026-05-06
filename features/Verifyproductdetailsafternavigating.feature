@tested

Feature: Product detail page verification

 Scenario Outline: Product detail page verification
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button
    When click on the product "<product_name>"
    Then user should see the product name "<product_name>"
    And user should see the product price "<price>"
    And click on the back to products
    And click on the hamburger
    And click on the logout button
    And close the browser

    Examples:
      | product_name                      | price   |
      | Sauce Labs Backpack               | $29.99  |
      | Sauce Labs Bike Light             | $9.99   |
      | Sauce Labs Bolt T-Shirt           | $15.99  |
      | Sauce Labs Fleece Jacket          | $49.99  |
      | Sauce Labs Onesie                 | $7.99   |
      | Test.allTheThings() T-Shirt (Red) | $15.99  |


