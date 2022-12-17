import pytest
from .pages.product_page import ProductPage
import time

FAIL_TEST_NO = 7
links = [str(i) for i in range(10) if i != FAIL_TEST_NO]
xlink = f'pytest.param({FAIL_TEST_NO}, marks=pytest.mark.xfail(reason="mistake on page"))'
links.insert(FAIL_TEST_NO, xlink)

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
