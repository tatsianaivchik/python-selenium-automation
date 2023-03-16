from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    EMPTY_CART_HEADER = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.sc-item-price-block span')

    def verify_cart_page_opens(self):
        self.verify_url_contains_query('https://www.amazon.com/gp/cart/')

    def verify_empty_cart_header_correct(self, header_text):
        self.verify_text(header_text, *self.EMPTY_CART_HEADER)

    def verify_product_name_n_price(self):
        self.verify_text(self.driver.product_name, *self.PRODUCT_NAME)
        self.verify_text(self.driver.product_price, *self.PRODUCT_PRICE)
