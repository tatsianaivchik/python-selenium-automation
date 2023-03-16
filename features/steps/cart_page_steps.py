from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify cart has correct product and price')
def verify_product_name_n_price(context):
    context.app.header.click_cart_icon()
    context.app.cart_page.verify_cart_page_opens()
    context.app.cart_page.verify_product_name_n_price()


@then('Verify "{header_text}" text present')
def verify_cart_empty(context, header_text):
    context.app.cart_page.verify_empty_cart_header_correct(header_text)
    # assert context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').is_displayed(), "'Your Amazon Cart is empty' field was not found"