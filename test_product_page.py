import random
import time
from string import ascii_letters, digits

import pytest

from .pages.locators import ProductPageLocators, CartPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_BAR)


class TestGuest:
    @staticmethod
    def _list_for_param_test() -> list[str]:
        FAIL_TEST_NO = 7
        links = [str(i) for i in range(10) if i != FAIL_TEST_NO]
        xlink = f'pytest.param({FAIL_TEST_NO}, marks=pytest.mark.xfail(reason="mistake on page"))'
        links.insert(FAIL_TEST_NO, xlink)
        return links

    def test_guest_cant_see_success_message(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, url)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_BAR)

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_cart(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_BAR)

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_cart()
        assert not page.is_element_present(*CartPageLocators.CART_CONTENTS)
        page.check_empty_cart()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_cart(self, browser):
        url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        time.sleep(3)
        page.check_name_in_cart()
        page.check_price_in_cart()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = LoginPage(browser, url)
        page.open()
        page.go_to_login_page()
        page.register_new_user(f'{str(time.time())}@dd.com', random.sample(digits + ascii_letters, 10))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, url)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_BAR)

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        time.sleep(3)
        page.check_name_in_cart()
        page.check_price_in_cart()
