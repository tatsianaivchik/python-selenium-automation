from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify that Sign In header is visible')
def verify_signin_page_header(context):
    context.app.signin_page.verify_signin_header()
    # expected_result = "Sign in"
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    # assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'


@then('Verify that email input field is present')
def verify_email_field(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field was not found'


@then('Verify Sign In page opens')
def verify_signin_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))