# Created by TANYA at 2/22/23
Feature: Amazon main page test

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon present
    When Click on ham menu

  Scenario: Footer and header has correct amount of links
    Given Open Amazon page
    Then Verify that footer has 42 links
    Then Verify that header has 29 links