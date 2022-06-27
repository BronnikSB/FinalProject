from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        add_basket.click()

    def check_add_name(self):
        product_name_and_price = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_AND_PRICE)
        self.should_be_text(product_name_and_price[0], "The shellcoder's handbook")
        self.should_be_text(product_name_and_price[2], "£9.9")




