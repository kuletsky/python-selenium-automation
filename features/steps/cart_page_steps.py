from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Verification
@then('Verify cart is empty')
def verify_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert actual_result in expected_result, f"Error! {actual_result}"
    print("\nVerify cart is successful!")