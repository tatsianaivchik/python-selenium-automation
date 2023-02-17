# Created by TANYA at 2/16/23
Feature: Amazon search tests

  Scenario: User can search for a coffee on Amazon
    Given Open Amazon page
    When Input text coffee
    When Click on search button
    Then Verify that text "coffee" is shown

