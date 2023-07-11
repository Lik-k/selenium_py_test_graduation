from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LINK_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_wrong")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email_wrong")
