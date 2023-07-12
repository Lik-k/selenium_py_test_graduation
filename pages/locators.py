from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LINK_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_wrong")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email_wrong")


class ProductPageLocators:
    LINK_PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_PRODUCT_HAS_BEEN_ADDED = (By.XPATH, "//div[1]/div[@class='alertinner ']")
    MESSAGE_PRICE = (By.XPATH, "//div[3]/div[@class='alertinner ']/p/strong")
    PRICE_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class='price_color']")
