from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Returns & Orders')
def click_returns(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@then('Verify that Sign In header is visible')
def verify_page_header(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'


@then('Verify that email input field is present')
def verify_email_field(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field was not found'


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Verify that Cart is empty')
def verify_cart_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').is_displayed(), "'Your Amazon Cart is empty' field was not found"


@then('Verify that {number} items shown')
def num_items_shown(context, number):
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert actual_result == str(number), f'Expected {number} but got {actual_result}'


@when('Click on the first item in Results')
def click_on_first_result(context):
        context.driver.find_element(By.CSS_SELECTOR, 'img.s-image[alt*=ZENNI]').click()


@when('Add product to the cart')
def add_product_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Check if product displays in the cart')
def check_number_of_cart_items(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()
    context.driver.find_element(By.CSS_SELECTOR,'img.sc-product-image[alt*=ZENNI]').is_displayed(), "Product not found"


