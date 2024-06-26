from selenium.webdriver.common.by import By
from behave import then


VERIFY_ITEM = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan-sc-odscpb-3']")


# Verify cart is empty
@then('Verify cart is empty')
def verify_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert actual_result in expected_result, f"Error! {actual_result}"
    print("\nVerify cart is successful!")


# Verify item is in the cart
@then('Verify item is in the cart')
def verify_item_is_in_the_cart(context):
    expected_result = 'item'
    actual_result = context.driver.find_element(*VERIFY_ITEM).text
    assert expected_result in actual_result, f"Error! {actual_result}"
