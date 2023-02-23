from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Add product to the cart')
def add_product_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()