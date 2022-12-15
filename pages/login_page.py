from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_URL

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "register button is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD1), "register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD2), "register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "register button is not presented"