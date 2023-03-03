from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price.priceToPay') #current price broken into 2 lines(test failed)

@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@when('Click on the first item in Results')
def click_on_first_result(context):
        context.driver.find_element(By.CSS_SELECTOR, 'img.s-image[alt*=ZENNI]').click()


@when('Store product name and price')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text
    print(f'Current product price: {context.product_price}')