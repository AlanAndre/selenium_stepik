from selenium.common.exceptions import NoSuchElementException

from pages.locators import BasePageLocators, CartPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=30):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_cart(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def check_empty_cart(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*CartPageLocators.EMPTY_CART_CONTENTS).text

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented,"\
                                                                     " probably unauthorised user"