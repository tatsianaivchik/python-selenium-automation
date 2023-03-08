from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

AMAZON_BEST_SELLERS = (By.ID, 'zg_banner_text')
BESTSELLERS_LINKS = (By.CSS_SELECTOR, '#zg_header a')
BESTSELLERS = (By.CSS_SELECTOR, 'a[href="/Best-Sellers/zgbs/ref=zg_bs_tab"]')
NEW_RELEASES = (By.CSS_SELECTOR, 'a[href="/gp/new-releases/ref=zg_bs_tab"]')
NEW_RELEASES2 = (By.CSS_SELECTOR, 'a[href="/gp/new-releases/ref=zg_bsnr_tab"]')
MOVERS_SHAKERS = (By.CSS_SELECTOR, 'a[href="/gp/movers-and-shakers/ref=zg_bsnr_tab"]')
MOVERS_SHAKERS2 = (By.CSS_SELECTOR, 'a[href="/gp/movers-and-shakers/ref=zg_bsms_tab"]')
MOST_WISHED_FOR = (By.CSS_SELECTOR, 'a[href="/gp/most-wished-for/ref=zg_bsms_tab"]')
MOST_WISHED_FOR2 = (By.CSS_SELECTOR, 'a[href="/gp/most-wished-for/ref=zg_mw_tab"]')
GIFT_IDEAS = (By.CSS_SELECTOR, 'a[href="/gp/most-gifted/ref=zg_mw_tab"]')
GIFT_IDEAS2 = (By.CSS_SELECTOR, 'a[href="/gp/most-gifted/ref=zg_mg_tab"]')
TAB_NAME = (By.ID, 'zg_banner_text')


@then('Verify that is BestSellers page')
def verify_that_is_bestsellers_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/bestsellers'))
    context.driver.find_element(*AMAZON_BEST_SELLERS)


@then('Verify that BestSellers page has {expected_amount} links')
def verify_bestsellers_link_count(context, expected_amount):
    bestsellers_links = context.driver.find_elements(*BESTSELLERS_LINKS)
    assert len(bestsellers_links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(bestsellers_links)}'


@then('Click on each link and verify that correct page opens')
def click_on_bestsellers_top_links(context):
    list_of_links = [BESTSELLERS, NEW_RELEASES, MOVERS_SHAKERS, MOST_WISHED_FOR, GIFT_IDEAS]
    list_of_links2 = [BESTSELLERS, NEW_RELEASES2, MOVERS_SHAKERS2, MOST_WISHED_FOR2, GIFT_IDEAS2]

    for i in range(len(list_of_links)):
        context.driver.find_element(*(list_of_links[i])).click()
        tab_name = context.driver.find_element(*(list_of_links2[i])).text
        print(tab_name)
        header_name = context.driver.find_element(*TAB_NAME).text
        print(header_name)
        if i == 1:
            assert "Amazon Hot " + tab_name == header_name
        else:
            assert "Amazon " + tab_name == header_name