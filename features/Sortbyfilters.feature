@tested

Feature: Verify the filters is working or not
Background: 
  Given I launch the browser
  When open the home page
  Then Enter the username and password
  And click on the login button

Scenario Outline: Verify the filter from A to Z
  Then click on the filterbutton
  And select the "<filter>"
  And Verify the products data is in correct filter from A to Z
  And click on the hamburger
  And click on the logout button
  And close the browser
  Examples:
      | filter|
      | Name (A to Z)  | 


Scenario Outline: Verify the filter from Z to A
  Then click on the filterbutton
  And select the "<filter>"
  And Verify the products data is in correct filter from Z to A
  And click on the hamburger
  And click on the logout button
  And close the browser
  Examples:
      | filter|
      | Name (Z to A)  | 

  
Scenario Outline: Verify the filter from price Low to High
  Then click on the filterbutton
  And select the "<filter>"
  And Verify the products data is in correct filter from Low to High
  And click on the hamburger
  And click on the logout button
  And close the browser
  Examples:
      | filter|
      |Price (low to high) | 

Scenario Outline: Verify the filter from price High to Low
  Then click on the filterbutton
  And select the "<filter>"
  And Verify the products data is in correct filter from High to Low
  And click on the hamburger
  And click on the logout button
  And close the browser
  Examples:
      | filter|
      |Price (high to low) | 

