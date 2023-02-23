from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Check if product displays in the cart')
def check_number_of_cart_items(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()
    context.driver.find_element(By.CSS_SELECTOR,'img.sc-product-image[alt*=ZENNI]').is_displayed(), "Product not found"


@then('Verify that Cart is empty')
def verify_cart_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').is_displayed(), "'Your Amazon Cart is empty' field was not found"