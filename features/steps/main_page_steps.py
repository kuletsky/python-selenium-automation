from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON = (By.CSS_SELECTOR, "use[href*='Cart.svg#Cart']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderContainer']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
VERIFY_ITEM = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan-sc-odscpb-3']")


# Open the Target main page
@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')
    context.wait.until(EC.presence_of_element_located(VERIFY_ITEM),
                       message='Cart is not open')
    # sleep(2)


# Click on cart
@when('Click on cart')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


# Verify header is shown
@then("Verify header is shown")
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


# Verify header has correct amount links
@then("Verify header has {expected_amount} links")
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    # for link in links:
    #     print(link.text)
    assert len(links) == expected_amount, f"Expected {expected_amount} links but got {len(links)}"


