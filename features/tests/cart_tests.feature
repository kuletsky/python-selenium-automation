Feature: Cart verify tests

  Scenario: Verify cart is empty
    Given Open Target main page
    When Click on cart
    Then Verify cart is empty


# Verify item is in the cart (HW 4)
  Scenario: Verify item is in the cart
    Given Open Target main page
    When Search for cup
    When Click on cart product
    When Click BTN Add to cart
    When Click BTN view cart
    Then Verify item is in the cart
