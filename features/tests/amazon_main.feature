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

  Scenario: Logged out user can navigate to Sign in page
    Given Open Amazon page
    When Click on Returns & Orders
    Then Verify Sign In page is opened

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present

  Scenario Outline: User can select and search in a special department
    Given Open Amazon page
    When Select department by alias <department>
    When Input text <search_word>
    When Click on search button
    Then Verify <department> department is selected
    Examples:
    |department      |search_word        |
    |amazonfresh     |Banana             |
    |petfoodexpress  |Dog food           |
    |automotive      |windshield wipers  |
