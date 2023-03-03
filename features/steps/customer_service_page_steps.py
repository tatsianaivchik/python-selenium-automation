from selenium.webdriver.common.by import By
from behave import given, when, then

WELCOME_AMAZON_CUSTOMER_SERVICE = (By.CSS_SELECTOR, 'h1.fs-heading.bolded')
ISSUE_CARD_CONTAINER = (By.CSS_SELECTOR, 'div.issue-card-container')
SEARCH_OUR_HELP_LIBRARY = (By.XPATH, '//h2[contains(text(),"Search our help")]')
SEARCH_OUR_HELP_FIELD = (By.ID, 'hubHelpSearchInput')
ALL_HELP_TOPICS = (By.XPATH, '//h2[contains(text(),"All help topics")]')
HELP_TOPICS_LIST = (By.CSS_SELECTOR, 'div.help-topics-list-wrapper ul.help-topics')


@then("Verify Customer Service's page UI elements are present")
def verify_cs_ui_elements(context):
    assert context.driver.find_element(*WELCOME_AMAZON_CUSTOMER_SERVICE).is_displayed(), 'Welcome Customer Service field was not found'
    assert context.driver.find_element(*ISSUE_CARD_CONTAINER).is_displayed(), 'Issue card container field was not found'
    assert context.driver.find_element(*SEARCH_OUR_HELP_LIBRARY).is_displayed(), 'Search our help LIBRARY was not found'
    assert context.driver.find_element(*SEARCH_OUR_HELP_FIELD).is_displayed(), 'Search our help FIELD was not found'
    assert context.driver.find_element(*ALL_HELP_TOPICS).is_displayed(), 'All help topics was not found'
    assert context.driver.find_element(*HELP_TOPICS_LIST).is_displayed(), 'Help topics list was not found'