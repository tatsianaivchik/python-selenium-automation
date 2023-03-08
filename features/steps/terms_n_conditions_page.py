from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

PRIVACY_NOTICE = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')
PRIVACY_HEADER = (By.XPATH, '//h1[contains(text(),"Privacy Notice")]')


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_tc_window(context):
    context.original_tc_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_privacy_notice_page(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))
    assert context.driver.find_element(*PRIVACY_HEADER).is_displayed()


@then('User can close new window and switch back to original')
def switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_tc_window)