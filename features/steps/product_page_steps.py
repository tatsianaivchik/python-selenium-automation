from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Add product to the cart')
def add_product_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    #context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray', 'Green', 'Khaki', 'Light-green', 'Orange', 'Pink', 'Purple', 'Red', 'Rose Red', 'Stripe Caramel', 'Stripe Gray', 'Stripe Green', 'Stripe Khaki', 'Stripe Red', 'Stripe Sapphire Blue', 'White', 'Yellow']

    actual_colors = []
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        #print('Current color: ', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'


@then('Verify user can select different colors')
def verify_user_can_pick_different_colors(context):
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Khaki Brown', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Khaki Brown', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash', 'Olive', 'Rinsed', 'Sage Green', 'Vintage Wash', 'Washed Black', 'Washed Grey']

    actual_colors = []
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        #print('Current color: ', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'