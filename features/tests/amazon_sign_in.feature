# Created by TANYA at 3/2/23
Feature: Amazon Sign in tests

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens