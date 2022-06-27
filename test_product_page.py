from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


def test_guest_can_add_product_to_basket(browser):
    link_page = ProductPageLocators.LINK_PRODUCT
    page = ProductPage(browser, link_page)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.check_add_name()