import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

FAIL_TEST_NO = 7
links = [str(i) for i in range(10) if i != FAIL_TEST_NO]
xlink = f'pytest.param({FAIL_TEST_NO}, marks=pytest.mark.xfail(reason="mistake on page"))'
links.insert(FAIL_TEST_NO, xlink)

@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_cart(browser, link):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.check_name_in_cart()
    page.check_price_in_cart()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_BAR)

def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, url)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_BAR)

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_BAR)
