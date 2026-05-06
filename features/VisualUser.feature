@tested

Feature: Visual user login and inventory verification

  Scenario Outline: Visual user can login successfully
    Given I launch the browser
    When open the home page
    Then verify the title "Swag Labs"
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then user should be redirected to the main page
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username    | password     |
    | visual_user | secret_sauce |

  Scenario Outline: Visual user inventory page displays all products
    Given I launch the browser
    When open the home page
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    Then the inventory page should display all 6 products
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username    | password     |
    | visual_user | secret_sauce |


  Scenario Outline: Visual user can add a product to cart
    Given I launch the browser
    When open the home page
    Then Enter the username "<username>"
    Then Enter the password "<password>"
    And click on the login button
    And add the "Sauce Labs Backpack" to cart
    Then verify the cart is updated or not
    And click on the hamburger
    And click on the logout button
    And close the browser
    Examples:
    | username    | password     |
    | visual_user | secret_sauce |

