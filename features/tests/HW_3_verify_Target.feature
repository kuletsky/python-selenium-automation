# Created by kuletsky at 01.04.2024
Feature: Target verify tests

  Scenario: Verify cart is empty
    Given Open Target main page
    When Click on cart
    Then Verify cart is empty

  Scenario: Verify SignIn is shown
    Given Open Target main page
    When Main page Sign In click
    When Side menu Sign In click
    Then Verify Sign In form is open
