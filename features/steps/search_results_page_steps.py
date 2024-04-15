import time

from selenium.webdriver.common.by import By
from behave import then, when
from time import sleep


SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
BTN_ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
BTN_CONFIRM_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/cart']")
SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, '[data-test*="SearchButton"]')


# Verify search results are shown for expected_item
@then("Verify search results are shown for {expected_item}")
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert expected_item in actual_text, f'Error! Text "{expected_item}" not in actual text "{actual_text}"'


# Search for product
@when('Search for {item}')
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)


# CClick on BTN "Add to cart"
@when('Click on BTN "Add to cart"')
def click_on_cart_product(context):
    # context.driver.find_element(*BTN_ADD_TO_CART).click()
    add_cart_btns = context.driver.find_elements(*BTN_ADD_TO_CART)
    for btn in add_cart_btns:
        btn.click()
        context.driver.find_element(*BTN_CONFIRM_ADD_TO_CART).click()
        context.driver.find_element(By.CSS_SELECTOR, "[aria-label='close']").click()
    # sleep(2)

# Confirm BTN "Add to cart"
@when('Confirm BTN "Add to cart"')
def click_on_cart_button(context):
    context.driver.find_element(*BTN_CONFIRM_ADD_TO_CART).click()
    sleep(2)


# # Click BTN view cart
# @when('Click BTN view cart')
# def click_on_view_button(context):
#     context.driver.find_element(*VIEW_CART_BTN).click()
