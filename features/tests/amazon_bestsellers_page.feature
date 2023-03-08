# Created by TANYA at 3/6/23
Feature: BestSellers page tests

  Scenario: BestSellers page has correct amount of links
    Given Open Amazon page
    When Click on BestSellers button
    Then Verify that is BestSellers page
    Then Verify that BestSellers page has 5 links


  Scenario: Verify that user can click on different links at the BestSellers page
    Given Open Amazon page
    When Click on BestSellers button
    Then Click on each link and verify that correct page opens
