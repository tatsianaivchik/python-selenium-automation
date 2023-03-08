from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

DOG_IMG = (By.CSS_SELECTOR, 'img#d')


@given('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on a dog image')
def click_image(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles # -> [..., ...]
    #print('\nAll windows: ', windows)
    context.driver.switch_to.window(windows[1])

    # context.current_window = context.driver.current_window_handle
    # print('After switch')
    # print(context.current_window)


@then('Verify blog is open')
def verify_blog_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/workplace'))


@then('Close blog')
def close_blog_page(context):
    context.driver.close()


@then('Return to original window')
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
