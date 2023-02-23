# Created by TANYA at 2/16/23
Feature: Amazon search tests

  Scenario Outline: User can search for a coffee on Amazon
    Given Open Amazon page
    When Input text <search_word>
    When Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word |search_result  |
    |coffee      |"coffee"       |
    |table       |"table"        |
    |mug         |"mug"          |
