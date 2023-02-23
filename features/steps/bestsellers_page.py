from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_BEST_SELLERS = (By.ID, 'zg_banner_text')
BESTSELLERS_LINKS = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a[href*="ref=zg_bs_tab"]')


@then('Verify that is BestSellers page')
def verify_that_is_bestsellers_page(context):
    context.driver.find_element(*AMAZON_BEST_SELLERS)


@then('Verify that BestSellers page has {expected_amount} links')
def verify_bestsellers_link_count(context, expected_amount):
    bestsellers_links = context.driver.find_elements(*BESTSELLERS_LINKS)
    assert len(bestsellers_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(bestsellers_links)}'
