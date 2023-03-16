from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')
    PRODUCT_PRICE = (By.ID, 'corePrice_feature_div')
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

    def store_product_name_n_price(self):
        self.driver.product_name = self.find_element(*self.PRODUCT_NAME).text
        self.driver.product_price = self.find_element(*self.PRODUCT_PRICE).text.replace('\n', '.')

    def add_product_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def open_product_page(self, product_id):
        self.driver.get(f'https://www.amazon.com/dp/{product_id}/')

    def verify_user_can_select_colors_for_product(self, expected_colors):
        self.select_different_colors_for_product_n_verify_name(*self.COLOR_OPTIONS, current_color=self.CURRENT_COLOR, expected_colors=expected_colors)