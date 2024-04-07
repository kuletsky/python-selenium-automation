Feature: Search verify tests

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
    |item     |expected_item  |
    |cup      |cup            |
    |key      |key            |
    |coffee   |coffee         |
    |flower   |flower         |

