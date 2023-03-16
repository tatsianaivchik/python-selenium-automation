from pages.base_page import Page
from selenium.webdriver.common.by import By

class SigninPage(Page):
    SIGNIN_HEADER = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_signin_header(self):
        self.verify_text("Sign in", *self.SIGNIN_HEADER)

    def verify_email_field_visible(self):
        self.find_element(*self.EMAIL_FIELD).is_displayed()

    def verify_signin_url(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin')
