from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_NAME = (By.CSS_SELECTOR, '#sc-active-cart li')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.sc-item-price-block span')


@then('Verify cart has correct product and price')
def verify_product_name(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in actual_name, f'Expected {context.product_name} but got {actual_name}'

    actual_price = context.driver.find_element(*PRODUCT_PRICE).text
    assert context.product_price == actual_price, f'Expected {context.product_price} but got {actual_price}'


@then('Verify that Cart is empty')
def verify_cart_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').is_displayed(), "'Your Amazon Cart is empty' field was not found"