@regressive
Feature: Footer navigation links

  Background:
    Given I launch the browser
    When open the home page
    Then Enter the username and password
    And click on the login button

  Scenario: Twitter link opens Twitter page
    Then click on the Twitter footer link
    And the new tab URL should contain "twitter.com" or "x.com"
    And close the browser

  Scenario: Facebook link opens Facebook page
    Then click on the Facebook footer link
    And the new tab URL should contain "facebook.com"
    And close the browser

  Scenario: LinkedIn link opens LinkedIn page
    Then click on the LinkedIn footer link
    And the new tab URL should contain "linkedin.com"
    And close the browser

  Scenario: Footer displays copyright text
    Then the footer copyright text should contain "Sauce Labs"
    And click on the hamburger
    And click on the logout button
    And close the browser
