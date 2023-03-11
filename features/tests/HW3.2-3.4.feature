# Created by TANYA at 2/16/23
Feature: Homework Amazon page tests

  Scenario: Check Amazon cart is empty
    Given Open Amazon page
    When Click on Cart icon
    Then Verify that Cart is empty
    And Verify that 0 items shown

  Scenario: Adding item in the cart
    Given Open Amazon page
    When Input text ZENNI glasses
    And Click on search button
    And Click on the first item in Results
    And Store product name and price
    And Add product to the cart
    Then Verify that 1 items shown
    And Verify cart has correct product and price


