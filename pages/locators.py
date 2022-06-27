from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():

    #Auth_form
    # USER_NAME = (By.CSS_SELECTOR, '#id_login-username')
    # USER_PASS = (By.CSS_SELECTOR, '#id_login-password')
    # BUTTON_AUTH = (By.CSS_SELECTOR, '[name="login_submit"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

    #Reg_form
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():

    LINK_PRODUCT = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_PRODUCT = (By.CSS_SELECTOR, '[value="Add to basket"]')
    PRODUCT_NAME_AND_PRICE_ADDED = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')



