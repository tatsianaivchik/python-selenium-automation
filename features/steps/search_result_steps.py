from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price.priceToPay') #current price broken into 2 lines(test failed)
SEARCH_RESULTS = (By.CSS_SELECTOR, 'div[cel_widget_id*="MAIN-SEARCH_RESULTS-"]')
PRODUCT_IMAGE = (By.CSS_SELECTOR, 'div[cel_widget_id*="MAIN-SEARCH_RESULTS-"] div.s-product-image-container')
PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, 'div[cel_widget_id*="MAIN-SEARCH_RESULTS-"] a.a-link-normal[href*="/gp/slredirect/"]')


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


@then('Verify that every product has name and image')
def verify_every_prod_has_name_and_image(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print('All results: ', all_products)

    for item in all_products:
        context.driver.find_element(*PRODUCT_IMAGE).is_displayed()
        context.driver.find_element(*PRODUCT_NAME_FIELD).is_displayed()