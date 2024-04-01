from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# open the Target main page
@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


# click on cart
@when('Click on cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "use[href*='/icons/assets/glyph/Cart.svg#Cart']").click()
    sleep(6)


# Verification
@then('Verify cart is empty')
def verify_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert actual_result in expected_result, f"Error! {actual_result}"
    print("\nVerify cart is successful!")


@when('Main page Sign In click')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()


@when('Side menu Sign In click')
def click_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify Sign In form is open')
def verify_sign_in(context):
    # Verification
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert actual_result in expected_result, f"Error! {actual_result}"
    print("\nVerify Sign In is successful!")

