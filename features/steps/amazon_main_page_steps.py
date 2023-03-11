from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
HEADER_LINKS = (By.CSS_SELECTOR, '#nav-xshop a.nav-a')
BESTSELLERS_BUTTON = (By.CSS_SELECTOR, 'a.nav-a[href*="/gp/bestsellers/"]')
CUSTOMER_SERVICE_BUTTON = (By.CSS_SELECTOR, 'a.nav-a[href*="=nav_cs_customerservice"]')
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click on Returns & Orders')
def click_orders_n_returns(context):
    # context.driver.find_element(By.ID, "nav-orders").click()
    context.app.header.click_orders_n_returns()


@when('Input text {text}')
def input_search_word(context, text):
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
    context.app.header.input_search_text(text)


@when('Click on search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@when('Click on BestSellers button')
def click_bestsellers_button(context):
    context.driver.find_element(*BESTSELLERS_BUTTON).click()


@when('Click on Customer Service button')
def click_customer_service_button(context):
    context.driver.find_element(*CUSTOMER_SERVICE_BUTTON).click()


@when('Click Sign In from popup')
def click_signin(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_BTN)).click()

    context.driver.wait.until(
        EC.visibility_of_element_located(SIGN_IN_BTN),
        message='Sign In btn not visible'
    ).click()


@when('Wait for {sec} seconds')
def wait_for_sec(context, sec):
    sleep(int(sec))

@then('Verify Sign In popup shown')
def verify_signin_popup_visible(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_BTN), message='Signin btn not found')


@then('Verify Sign In popup disappeared')
def verify_signin_popup_not_visible(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_BTN), message='Signin btn did not disappear')


@then('Verify that {number} items shown')
def num_items_shown(context, number):
    context.driver.implicitly_wait(2)
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert actual_result == str(number), f'Expected {number} but got {actual_result}'


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    context.driver.refresh()


@when('Click on ham menu')
def click_ham_menu(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    context.ham_menu.click()


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
       footer_links = context.driver.find_elements(*FOOTER_LINKS)
       assert len(footer_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(header_links)}'