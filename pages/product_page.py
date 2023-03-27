from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')
    PRODUCT_PRICE = (By.ID, 'corePrice_feature_div')
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
    NEW_ARRIVALS = (By.CSS_SELECTOR, '#nav-subnav a[aria-label="New Arrivals"]')
    NEW_ARRIVALS_SELECTION = (By.CSS_SELECTOR, 'div.nav-template.nav-flyout-content div.mm-column a.mm-merch-panel[href*="fashion-womens"]')

    def store_product_name_n_price(self):
        self.driver.product_name = self.find_element(*self.PRODUCT_NAME).text
        self.driver.product_price = self.find_element(*self.PRODUCT_PRICE).text.replace('\n', '.')

    def add_product_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def open_product_page(self, product_id):
        self.driver.get(f'https://www.amazon.com/dp/{product_id}/')

    def verify_user_can_select_colors_for_product(self, expected_colors):
        self.select_different_colors_for_product_n_verify_name(*self.COLOR_OPTIONS, current_color=self.CURRENT_COLOR, expected_colors=expected_colors)

    def hover_new_arrivals(self):
        new_arrivals_tab = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element((new_arrivals_tab))
        actions.perform()

    def verify_user_sees_new_arrivals_selections(self):
        self.wait_for_element_appear(self.NEW_ARRIVALS_SELECTION)