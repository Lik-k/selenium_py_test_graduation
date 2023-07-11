from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link = LoginPageLocators.LINK_LOGIN_PAGE
        assert "login" in link, f"expected '{'login'}' to be substring of '{link}'"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert LoginPageLocators.LOGIN_FORM, "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert LoginPageLocators.REGISTRATION_FORM, "Registration form is not presented"