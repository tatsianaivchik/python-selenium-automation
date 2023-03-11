from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_N_RETURNS = (By.ID, "nav-orders")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders_n_returns(self):
        self.click(*self.ORDERS_N_RETURNS)