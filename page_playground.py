class Page:
    def __init__(self):
        self.url = "www.amazon.com"

    def open_url(self):
        print('Url opening', self.url)

    def close(self):
        print('Closing the page', self.url)

class LoginPage(Page):
    def open_login(self):
        print('Login page opens')

    def close(self):
        print('Closing the login page', self.url)

p = Page()
# p.open_url()
# p.close()

login_page = LoginPage()
login_page.close()
# login_page.open_login()
#
# print(p.url)
# print(LoginPage().url)