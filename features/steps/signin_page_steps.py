from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Sign In page is opened')
def verify_email_field(context):
    context.app.signin_page.verify_email_field_visible()
    context.app.signin_page.verify_signin_header()
    context.app.signin_page.verify_signin_url()
    # assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field was not found'


@then('Verify Sign In page opens')
def verify_signin_opened(context):
    context.app.signin_page.verify_signin_url()
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))