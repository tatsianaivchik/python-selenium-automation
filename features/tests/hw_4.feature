# Created by TANYA at 2/22/23
Feature: Homework_4 tests
  BestSellers page test
  Customer Service’s page UI elements test

  Scenario: BestSellers page has correct amount of links
    Given Open Amazon page
    When Click on BestSellers button
    Then Verify that is BestSellers page
    Then Verify that BestSellers page has 5 links

  Scenario: Verify that Customer Service's page UI elements are present
    Given Open Amazon page
    When Click on Customer Service button
    Then Verify Customer Service's page UI elements are present

