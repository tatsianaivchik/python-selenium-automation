from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
HEADER_LINKS = (By.CSS_SELECTOR, '#nav-xshop a.nav-a')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Returns & Orders')
def click_returns(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Verify that {number} items shown')
def num_items_shown(context, number):
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert actual_result == str(number), f'Expected {number} but got {actual_result}'


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
       footer_links = context.driver.find_elements(*FOOTER_LINKS)
       assert len(footer_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(header_links)}'