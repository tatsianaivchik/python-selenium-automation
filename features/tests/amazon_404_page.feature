# Created by TANYA at 3/4/23
Feature: Tests for 404 page

  Scenario: User is able to navigate to amazon blog from 404 page
    Given Open Amazon product B07KJZ8HCW88888 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is open
    And Close blog
    And Return to original window