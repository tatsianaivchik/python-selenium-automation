# Created by TANYA at 3/2/23
Feature: Test for product page

  Scenario: User can select colors
    Given Open Amazon product B08JHKQPBV page
    Then Verify user can click through colors

  Scenario: User can select different colors of Men Jeans
    Given Open Amazon product B07BJL37GD page
    Then Verify user can select different colors

    Scenario: Verify that user can see New Arrivals options
      Given Open Amazon product B074TBCSC8 page
      When Hover over New Arrivals Tab
      Then Verify that user sees category Women's