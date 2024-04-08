from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGNIN = (By.XPATH, "//span[text()='Sign into your Target account']")


@then('Verify SignIn form is open')
def verify_sign_in(context):
    # Verification
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(*SIGNIN).text
    assert actual_result in expected_result, f"Error! {actual_result}"
    print("\nVerify Sign In is successful!")