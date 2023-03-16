from pages.base_page import Page
from selenium.webdriver.common.by import By

class BestsellersPage(Page):
    AMAZON_BEST_SELLERS = (By.ID, 'zg_banner_text')
    BESTSELLERS_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    TAB_NAME = (By.ID, 'zg_banner_text')

    def verify_bestsellers_page_opens(self):
        self.verify_url_contains_query('https://www.amazon.com/gp/bestsellers')
        self.find_element(*self.AMAZON_BEST_SELLERS)

    def verify_bestsellers_link_count(self, expected_amount):
        self.verify_count_of_links(expected_amount, *self.BESTSELLERS_LINKS)

    def click_n_verify_all_bestsellers_links(self):
        self.click_through_links_n_verify_text(*self.BESTSELLERS_LINKS, name_locator=self.TAB_NAME)