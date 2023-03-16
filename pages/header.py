from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_N_RETURNS = (By.ID, "nav-orders")
    CART_ICON = (By.ID, 'nav-cart-count-container')
    NUM_ITEMS_IN_CART = (By.ID, 'nav-cart-count')
    BESTSELLERS_BUTTON = (By.CSS_SELECTOR, 'a.nav-a[href*="/gp/bestsellers/"]')
    SIGNIN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders_n_returns(self):
        self.click(*self.ORDERS_N_RETURNS)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def num_items_in_cart(self, expected_number):
        self.driver.implicitly_wait(2)
        self.verify_text(expected_number, *self.NUM_ITEMS_IN_CART)

    def click_bestsellers_button(self):
        self.click(*self.BESTSELLERS_BUTTON)

    def click_signin_from_popup(self):
        self.wait_for_element_appear(self.SIGNIN_POPUP_BTN).click()
