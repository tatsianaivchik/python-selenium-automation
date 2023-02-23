# Created by TANYA at 2/16/23
Feature: Homework Amazon page tests

  Scenario: Logged out user can navigate to Sign in page
    Given Open Amazon page
    When Click on Returns & Orders
    Then Verify that Sign In header is visible
    And Verify that email input field is present

  Scenario: Check Amazon cart is empty
    Given Open Amazon page
    When Click on Cart icon
    Then Verify that Cart is empty
    And Verify that 0 items shown

  Scenario: Adding item in the cart
    Given Open Amazon page
    When Input text glasses
    And Click on search button
    When Click on the first item in Results
    And Add product to the cart
    Then Verify that 1 items shown
    And Check if product displays in the cart


