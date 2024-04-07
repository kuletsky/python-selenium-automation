Feature: Cart verify tests

  Scenario: Verify cart is empty
    Given Open Target main page
    When Click on cart
    Then Verify cart is empty
