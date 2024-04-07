from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, '[data-test*="SearchButton"]')
CART_ICON = (By.CSS_SELECTOR, "use[href*='Cart.svg#Cart']")
MAIN_SIGNIN = (By.XPATH, "//span[text()='Sign in']")
MENU_SIGNIN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")


# Open the Target main page
@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


# Search for product
@when('Search for {item}')
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)


# Click on cart
@when('Click on cart')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


# Main page SignIn click
@when('Main page SignIn click')
def click_sign_in(context):
    context.driver.find_element(*MAIN_SIGNIN).click()


# Side menu Sign In click
@when('Side menu SignIn click')
def click_side_menu(context):
    context.driver.find_element(*MENU_SIGNIN).click()
    sleep(6)
