from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        add_basket.click()

    def check_add_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.should_be_text(product_name, "The shellcoder's handbook")




